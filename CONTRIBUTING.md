# Contributing

Keep the core research methodology in `plugins/research-dossier/skills/research/` and put platform-specific installation details in `adapters/`. Do not fork the evidence policy for one platform.

Before opening a change:

1. Add or update a behavior test when changing scripts or repository contracts.
2. Run `python3 -m unittest discover -v`.
3. Run the bundled skill validator for every changed skill.
4. Run the Codex plugin validator for manifest or packaged-path changes.
5. Update `CHANGELOG.md` for user-visible behavior.
6. Keep generated user projects out of the repository unless they are deliberately added as an example.
