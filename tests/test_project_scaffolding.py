import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "plugins" / "research-dossier" / "scripts" / "new_research_project.py"


class ProjectScaffoldingTests(unittest.TestCase):
    def test_new_project_creates_resumable_layout_without_overwriting_input(self):
        self.assertTrue(SCRIPT.is_file())
        with tempfile.TemporaryDirectory() as directory:
            workdir = Path(directory)
            command = [
                "python3",
                str(SCRIPT),
                "--workdir",
                str(workdir),
                "--slug",
                "immunity-to-change",
                "--title",
                "Иммунитет к изменениям",
            ]
            first = subprocess.run(command, text=True, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            project = workdir / "research" / "immunity-to-change"
            for relative in (
                "PROJECT.md",
                "input/original-material.md",
                "working/brief.md",
                "working/question-map.md",
                "working/source-ledger.md",
                "working/findings.md",
                "working/creative-lab.md",
                "working/open-questions.md",
                "output/research.md",
                "reviews/factcheck.md",
            ):
                self.assertTrue((project / relative).is_file(), relative)
            self.assertIn("Карта исследовательских задач", (project / "working" / "question-map.md").read_text())
            self.assertIn("карточками", (project / "working" / "findings.md").read_text())

            original = project / "input" / "original-material.md"
            original.write_text("user material")
            second = subprocess.run(command, text=True, capture_output=True)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(original.read_text(), "user material")

    def test_project_state_reports_last_completed_stage(self):
        self.assertTrue(SCRIPT.is_file())
        state_script = SCRIPT.parent / "project_state.py"
        self.assertTrue(state_script.is_file())
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "research" / "demo"
            (project / "working").mkdir(parents=True)
            (project / "PROJECT.md").write_text("status: researching\nlast_completed: question-map\n")
            result = subprocess.run(
                ["python3", str(state_script), str(project)],
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("question-map", result.stdout)
            self.assertIn("working/findings.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
