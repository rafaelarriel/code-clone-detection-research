# Code Clone Detection 1.1

Instruction-only Agent Skill (no executable detector). Renamed-vs-identical body rules, multigranular reporting, candidate audit, and detection/refactoring separation.

Install the **folder** `code-clone-detection` in `$HOME/.agents/skills/` for Codex or `$HOME/.claude/skills/` for Claude Code. Project scope: `.agents/skills/` or `.claude/skills/`. Replace the v1.0 folder for v1.1 experiments; **keep an archived copy of v1.0 outside agent discovery paths**.

Use: `Use $code-clone-detection to analyze src/ ...` (Codex) or `/code-clone-detection` where available.

Important for experimental controls: global skills may be loaded automatically. Run baseline with skill folders removed/disabled in *all discovery locations*, preferably using isolated agent profiles. Keep source and private answer key apart. This skill does not contain benchmark-specific answers.
