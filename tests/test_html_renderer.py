import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "plugins" / "research-dossier" / "scripts" / "render_html.py"


class HtmlRendererTests(unittest.TestCase):
    def test_renderer_preserves_content_and_adds_navigation_sources_and_copy_controls(self):
        self.assertTrue(SCRIPT.is_file())
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "research.md"
            output = Path(directory) / "research.html"
            markdown = """# Research\n\n## Key idea\n\nA useful thesis. [Source](https://example.com/source)\n\n| Concept | Use |\n| --- | --- |\n| Immunity | Show conflict |\n\n> A short quote\n\n## Reviews\n\nFactcheck pending.\n"""
            source.write_text(markdown)
            result = subprocess.run(
                ["python3", str(SCRIPT), str(source), str(output)],
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            html = output.read_text()
            self.assertIn("Key idea", html)
            self.assertIn("example.com/source", html)
            self.assertIn("table", html)
            self.assertIn("copy", html.lower())
            self.assertIn("Factcheck pending", html)
            self.assertNotIn("evidence-proven", html)
            self.assertEqual(source.read_text(), markdown)

    def test_renderer_keeps_parentheses_inside_doi_urls(self):
        self.assertTrue(SCRIPT.is_file())
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "research.md"
            output = Path(directory) / "research.html"
            source.write_text("[DOI](https://doi.org/10.1016/S0065-2601(06)38002-1)\n")
            result = subprocess.run(
                ["python3", str(SCRIPT), str(source), str(output)],
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(
                'href="https://doi.org/10.1016/S0065-2601(06)38002-1"',
                output.read_text(),
            )

    def test_copy_payload_is_plain_text_and_keeps_source_url(self):
        self.assertTrue(SCRIPT.is_file())
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "research.md"
            output = Path(directory) / "research.html"
            source.write_text("**Claim** with [source](https://example.com/paper)\n")
            result = subprocess.run(
                ["python3", str(SCRIPT), str(source), str(output)],
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            html = output.read_text()
            self.assertIn(
                'data-copy="&quot;Claim with source (https://example.com/paper)&quot;"',
                html,
            )
            self.assertNotIn(
                'data-copy="&quot;**Claim** with [source]',
                html,
            )


if __name__ == "__main__":
    unittest.main()
