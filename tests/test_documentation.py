import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_readme_documents_installation_and_operating_contract(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.is_file())
        text = readme.read_text().lower()
        for phrase in (
            "chatgpt",
            "codex",
            "claude code",
            "./research/",
            "audience",
            "resume",
            "html",
            "factcheck",
            "web search",
            "privacy",
            "иммунитет к изменениям",
        ):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()

