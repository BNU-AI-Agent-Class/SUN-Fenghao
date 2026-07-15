"""不调用模型也能跑的 Day2 验收测试。"""
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch

import agent_search
from hw2_demo.notes_app import analyze


class SearchToolTests(unittest.TestCase):
    def test_search_returns_file_line_and_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample.py"
            target.write_text("first\nadd_note('hello')\n", encoding="utf-8")
            result = agent_search.search("add_note", tmp)
            self.assertIn("sample.py:2", result)
            self.assertIn("add_note", result)

    def test_search_handles_no_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "sample.txt").write_text("hello", encoding="utf-8")
            self.assertEqual(agent_search.search("missing", tmp), "没有找到：missing")

    def test_parse_code_fence(self):
        action = agent_search.parse_action('```json\n{"done":"ok"}\n```')
        self.assertEqual(action, {"done": "ok"})


class CapstoneTests(unittest.TestCase):
    def test_summary_without_tags_does_not_crash(self):
        notes = [{"text": "没有标签", "tags": [], "created": "2026-07-15T00:00:00"}]
        with patch.object(analyze, "all_notes", return_value=notes):
            with patch.object(analyze, "tag_counts", return_value=[]):
                self.assertEqual(analyze.summary(), "共有 1 条笔记。\n还没有任何标签。")


if __name__ == "__main__":
    unittest.main(verbosity=2)

