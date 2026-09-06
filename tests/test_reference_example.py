import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "immunity-to-change"


class ReferenceExampleTests(unittest.TestCase):
    def test_reference_example_has_required_research_layers(self):
        for relative in (
            "README.md",
            "input.md",
            "question-map.md",
            "research.md",
            "source-ledger.md",
            "creative-lab.md",
        ):
            self.assertTrue((EXAMPLE / relative).is_file(), relative)
        research = (EXAMPLE / "research.md").read_text()
        self.assertIn("данные о выборе медицинских и пенсионных планов", research)
        self.assertNotIn("health plans и retirement programs", research)
        for phrase in (
            "[ДОКАЗАНО]",
            "[ИНТЕРПРЕТАЦИЯ]",
            "[КРЕАТИВНАЯ ГИПОТЕЗА]",
            "Цитаты",
            "Книги",
            "Кейсы",
            "Перевод:",
            "Оригинал:",
        ):
            self.assertIn(phrase, research)
        concepts = re.findall(r"^###\s+\d+\.", research, re.MULTILINE)
        self.assertEqual(len(concepts), 10)


if __name__ == "__main__":
    unittest.main()
