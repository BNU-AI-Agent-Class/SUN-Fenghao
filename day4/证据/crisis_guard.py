"""Deterministic crisis detection and response guardrails."""

from __future__ import annotations

from dataclasses import dataclass

from qiming_core.schemas.c0 import C0Response, StateUpdate


@dataclass(frozen=True)
class CrisisAssessment:
    kind: str = "none"
    level: str = "green"
    matched_signals: tuple[str, ...] = ()

    @property
    def active(self) -> bool:
        return self.kind != "none"


class CrisisGuard:
    """Adds a deterministic safety layer around the model's own judgement."""

    SELF_HARM_SIGNALS = (
        "不想活",
        "结束这一切",
        "结束掉",
        "自杀",
        "伤害自己",
        "自残",
        "不想醒来",
        "不用醒来",
        "不能保证自己安全",
        "没法保证自己安全",
        "不太能保证自己安全",
        "已经准备好了",
    )
    HARM_OTHERS_SIGNALS = (
        "伤害那个人",
        "伤害别人",
        "杀了他",
        "杀了她",
        "怎么报复",
        "报复他",
        "报复她",
    )

    def assess(self, text: str) -> CrisisAssessment:
        normalized = "".join(text.lower().split())
        self_harm = tuple(signal for signal in self.SELF_HARM_SIGNALS if signal in normalized)
        if self_harm:
            return CrisisAssessment(kind="self_harm", level="red", matched_signals=self_harm)
        harm_others = tuple(signal for signal in self.HARM_OTHERS_SIGNALS if signal in normalized)
        if harm_others:
            return CrisisAssessment(kind="harm_others", level="red", matched_signals=harm_others)
        return CrisisAssessment()

    def entry_instruction(self, assessment: CrisisAssessment) -> str:
        if not assessment.active:
            return ""
        return (
            "[确定性安全入口已触发] 当前消息含高风险信号。不得提供自伤、伤人、规避发现或报复方法；"
            "最终回复必须优先确认眼前安全，明确转向现实支持，并提供 12356 与紧急情况下的 110/120。"
            "不要答应替代现实帮助，也不要只做情绪陪伴。"
        )

    def enforce(self, message: str, c0: C0Response) -> tuple[C0Response, CrisisAssessment, bool]:
        assessment = self.assess(message)
        model_flags = set(c0.state_update.risk_flags)
        model_red = c0.state_update.safety_level == "red"
        self_harm_flag = bool(model_flags & {"self_harm_signal", "suicide_intent", "passive_suicidal_ideation", "safety_risk"})
        harm_others_flag = "harm_to_others_signal" in model_flags

        if not assessment.active and not model_red and not self_harm_flag and not harm_others_flag:
            return c0, assessment, False

        kind = assessment.kind
        if kind == "none":
            kind = "harm_others" if harm_others_flag else "self_harm"
            assessment = CrisisAssessment(kind=kind, level="red", matched_signals=("model_risk_state",))

        segments = self._harm_others_segments() if kind == "harm_others" else self._self_harm_segments()
        flags = list(dict.fromkeys([*c0.state_update.risk_flags, f"deterministic_{kind}_guard"]))
        guarded = c0.model_copy(
            update={
                "final_reply_ready": True,
                "response_mode": "final",
                "ui_status": "",
                "reply": "\n\n".join(segments),
                "segments": segments,
                "tool_calls": [],
                "state_update": StateUpdate(
                    relationship_stage_judge=c0.state_update.relationship_stage_judge,
                    did_self_disclosure=False,
                    memory_worth_saving=True,
                    safety_level="red",
                    risk_flags=flags,
                ),
            }
        )
        return guarded, assessment, True

    @staticmethod
    def _self_harm_segments() -> list[str]:
        return [
            "我很认真地听见了：你现在可能正处在危险里。先别一个人扛，也先不要做任何伤害自己的事。",
            "请现在就联系一个能到你身边的人，直接告诉对方：‘我现在不能保证自己的安全，请来陪我。’同时把可能伤害自己的东西放远，尽量去有人的地方。",
            "如果危险就在眼前，请立即拨打 110 或 120；也可以拨打全国统一心理援助热线 12356。若拨号很难，就先把这段话发给室友、同学、家人、辅导员或宿管。",
            "我可以继续陪你把下一步说清楚，但我不能替代现实中的紧急帮助。你现在是一个人吗？手边有没有已经准备好的工具或药物？",
        ]

    @staticmethod
    def _harm_others_segments() -> list[str]:
        return [
            "我听见你现在非常愤怒，但我不能帮你伤害或报复任何人。我们先把眼前的危险降下来。",
            "请先和对方拉开距离，把刀具、药物或其他可能造成伤害的东西放下并离开现场；找一个可信任的人来陪你。",
            "如果你觉得自己可能马上失控，请立即拨打 110，或联系校园保卫处、辅导员、宿管等能到场的人。",
            "我可以继续听你说发生了什么。你现在和那个人在同一个地方吗？手边有没有可能伤人的东西？",
        ]
