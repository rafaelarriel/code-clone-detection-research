# Code Clone Detection — Agent Skill

Instruction-only, agent-agnostic skill for finding candidate Type 1–4 code clones and advising on refactoring without automatically editing code.

## Contents

- `SKILL.md`: required entrypoint and workflow.
- `references/clone-types.md`: practical Type 1–4 taxonomy and limitations.
- `references/detection-guidelines.md`: investigation and false-positive filters.
- `references/refactoring-guidelines.md`: cautious guidance for refactoring.
- `references/report-template.md`: standardized review report.
- `references/evaluation-protocol.md`: proposed academic comparison protocol.
- `examples/manual-test-cases.md`: teaching/smoke-test cases, **not** a scientific benchmark.

## Install on a project

Copy the entire `code-clone-detection` directory to one of these destinations (both may coexist; use the same content):

| Agent | Project-local destination | User-wide destination |
|---|---|---|
| OpenAI Codex | `.agents/skills/code-clone-detection/` | `~/.agents/skills/code-clone-detection/` |
| Claude Code | `.claude/skills/code-clone-detection/` | `~/.claude/skills/code-clone-detection/` |

Paths follow the published documentation as of November 2026. Other compatible agents may use different discovery paths. For a Windows home directory, `~` refers to the user's home path (e.g. `C:\Users\<username>`).

## Example request

> Use the `code-clone-detection` skill to review `src/` for Types 1–4 clones. Provide an evidence-based report with file/line ranges, confidence and refactoring suggestions. Do not modify any files.

## Safety and scope

- This skill **only gives instructions** to an agent; it does not provide AST detection, scripts, a neural model, automated equivalence proofs or guaranteed findings.
- The quality and coverage depend on the host agent, its access to code and its context limits.
- A semantic clone is an investigatory finding until supported by appropriate evidence and tests.
- Do not publish repository secrets or sensitive proprietary code in reports.

## Specification and docs

- Agent Skills specification: https://agentskills.io/specification
- OpenAI skill guidance: https://learn.chatgpt.com/docs/build-skills
- Claude skill documentation: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

## Academic use

Use the evaluation protocol to compare like-for-like agent baselines. No experiments have been conducted or metrics verified as part of this distribution.
