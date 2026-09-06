import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "research-dossier"


class RepositoryContractTests(unittest.TestCase):
    def test_codex_plugin_manifest_has_required_identity(self):
        manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
        self.assertTrue(manifest_path.is_file())
        manifest = json.loads(manifest_path.read_text())
        self.assertEqual(manifest["name"], "research-dossier")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+(?:[-+].*)?$")
        self.assertTrue(manifest["description"])
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertTrue(manifest["interface"]["displayName"])
        self.assertTrue(manifest["interface"]["shortDescription"])
        self.assertTrue(manifest["interface"]["longDescription"])

    def test_main_skill_contains_research_contract(self):
        skill_path = PLUGIN / "skills" / "research" / "SKILL.md"
        self.assertTrue(skill_path.is_file())
        text = skill_path.read_text()
        for phrase in (
            "question-map.md",
            "confirmation",
            "10",
            "source",
            "checkpoint",
            "Иммунитет к изменениям",
            "research-card.md",
            "scenario-synthesis.md",
            "five options generated for this topic",
            "editorial card",
            "2–4 alternatives",
            "Не используйте повторяющиеся",
            "Keep internal routing and instruction loading invisible",
        ):
            self.assertIn(phrase, text)
        self.assertNotIn("[TODO", text)

    def test_research_references_match_reader_facing_contract(self):
        output_format = (PLUGIN / "skills" / "research" / "references" / "output-format.md").read_text()
        evidence_policy = (PLUGIN / "skills" / "research" / "references" / "evidence-policy.md").read_text()
        for phrase in ("Коротко: 7–10", "Как из материала можно собрать ролик", "Карточка важного материала"):
            self.assertIn(phrase, output_format)
        self.assertIn("не используйте повторяющиеся статусные теги", evidence_policy)
        self.assertNotIn("[ДОКАЗАНО]", output_format)

    def test_companion_skills_are_independently_routable(self):
        expected = {
            "research-critic": "critic",
            "research-factcheck": "fact",
            "research-editorial-review": "editorial",
            "research-concept-refiner": "concept",
            "research-html": "HTML",
        }
        for directory, marker in expected.items():
            skill_path = PLUGIN / "skills" / directory / "SKILL.md"
            self.assertTrue(skill_path.is_file(), directory)
            text = skill_path.read_text().lower()
            self.assertIn(marker.lower(), text)
            self.assertIn("research.md", text)


if __name__ == "__main__":
    unittest.main()
