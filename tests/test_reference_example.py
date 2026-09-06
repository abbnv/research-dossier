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
        self.assertIn("выбор медицинских планов сотрудников Harvard", research)
        self.assertNotIn("health plans и retirement programs", research)
        for phrase in (
            "Коротко: что мы узнали",
            "Рекомендуемая сборка",
            "Карточка 1.",
            "Сравнение концепций",
            "Кейсы и истории",
            "Банк цитат",
            "Книги, видео, фильмы",
            "Метафоры и короткие иллюстрации",
            "Десять безумных концепций",
            "Что ещё нужно проверить",
            "Перевод:**",
            "Оригинал:**",
        ):
            self.assertIn(phrase, research)
        for old_tag in (
            "[ДОКАЗАНО]",
            "[ПОДТВЕРЖДАЕТСЯ]",
            "[ИНТЕРПРЕТАЦИЯ]",
            "[КРЕАТИВНАЯ ГИПОТЕЗА]",
            "[НАТЯНУТО]",
        ):
            self.assertNotIn(old_tag, research)
        concepts_block = research.split("## 11. Десять безумных концепций", 1)[1].split("## 12.", 1)[0]
        self.assertEqual(len(re.findall(r"^\d+\. ", concepts_block, re.MULTILINE)), 10)


if __name__ == "__main__":
    unittest.main()
