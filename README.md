# Agent Workflow Skills

**Each skill now has its own repository.** Use the standalone repositories below
for installation, issues and updates. This collection remains available for existing
links; the independent repositories are the maintained homes.

| Skill | Standalone repository |
| --- | --- |
| Project Artifact Cleanup | [ShiYuPro/project-artifact-cleanup](https://github.com/ShiYuPro/project-artifact-cleanup) |
| Localize Naturally | [ShiYuPro/localize-naturally](https://github.com/ShiYuPro/localize-naturally) |
| Evidence-Bound Execution | [ShiYuPro/evidence-bound-execution](https://github.com/ShiYuPro/evidence-bound-execution) |
| Multimodel Chinese Copywriting | [ShiYuPro/multimodel-chinese-copywriting](https://github.com/ShiYuPro/multimodel-chinese-copywriting) |
| Fast Deployment Execution | [ShiYuPro/fast-deployment-execution](https://github.com/ShiYuPro/fast-deployment-execution) |


Practical skills for the work AI agents tend to leave unfinished: cleaning their
own scratch files, preserving localization structure, following corrections,
verifying copy, and closing out a release.

Start with **[Project Artifact Cleanup](https://github.com/ShiYuPro/project-artifact-cleanup)**
if your agent keeps leaving screenshots, experiments, logs, and outdated drafts
around your project. It manages only artifacts you deliberately enroll. It does
not guess which source files are safe to delete.

| Skill | Use it when | Included tooling |
| --- | --- | --- |
| [Project Artifact Cleanup](https://github.com/ShiYuPro/project-artifact-cleanup) | Agent scratch and review files keep accumulating | Preview, retention, pinning, recovery before expiry, guarded sweep |
| [Localize Naturally](https://github.com/ShiYuPro/localize-naturally) | UI translations lose meaning, placeholders, or layout fit | printf/template and ICU checks; 12 starter locale profiles |
| [Evidence-Bound Execution](https://github.com/ShiYuPro/evidence-bound-execution) | Requirements are acknowledged but disappear from the result | Lightweight execution card; optional versioned evidence gate |
| [Multimodel Chinese Copywriting](https://github.com/ShiYuPro/multimodel-chinese-copywriting) | You want an external Chinese model to draft and an agent to verify | Explicit provider configuration, offline dry run, no automatic retries |
| [Fast Deployment Execution](https://github.com/ShiYuPro/fast-deployment-execution) | Release work repeats checks without reaching a verified result | Optional timed command runner; project-owned release procedure |

## Install only what you need

Install from the maintained standalone repository with Node.js and npm:

```sh
npx skills add ShiYuPro/project-artifact-cleanup --skill project-artifact-cleanup
```

Choose Codex or Claude Code when prompted. For another skill, replace both
`project-artifact-cleanup` occurrences with its repository name from the table.
Each standalone README also includes a Git-only installation option.
The copies in this collection are retained for compatibility and are not updated.

Invoke the installed skill by name, for example:

> Use $project-artifact-cleanup to inspect this project's agent artifacts. Start
> with a preview and help me choose a retention policy. Do not delete anything yet.

The folders use the `SKILL.md` format. `agents/openai.yaml` adds Codex UI metadata.
Other agents may use the instructions, but discovery and scheduling depend on the
host. Compatibility with every agent is not claimed.

## What cleanup actually does

```text
Agent creates scratch → active task payload
                              │ task finished
                              ▼
                        retained payload
                        │             │
                  restore + pin   expiry + sweep
                        │             │
                        ▼             ▼
                  recovered copy   deletion
```

Active, pinned, changed, malformed, and unsafe groups are protected. Zero-day
cleanup and sweeps preview by default; `--apply` is an explicit mutation flag.
Recovery is available only while retained bytes still exist. The store is local
and should not contain production data or unique deliverables. File classification
and adoption require judgment; the script cannot infer every project dependency.

See [first-use commands and policy setup](https://github.com/ShiYuPro/project-artifact-cleanup/blob/main/references/setup.md).
There is **no installed scheduler** and no inherited deletion authorization.

## Requirements

- Python 3.9+ for the helpers; no Python package dependencies.
- macOS/Linux/WSL for cleanup (`fcntl` locking); native Windows is not supported
  for that helper.
- Node.js 20+ with full ICU for ICU validation, plus the pinned FormatJS parser:
  `npm ci --ignore-scripts` in `skills/localize-naturally/scripts`.
- External copywriting requires your own provider account, supported model ID,
  HTTPS endpoint, and authorization for data transfer and API costs. An offline
  dry run needs no credentials.
- Deployment commands and provider authentication belong to your project. The
  runner is not a sandbox, provider adapter, distributed lock or rollback engine.

## Try without external services

The maintained cleanup repository includes a [runnable demo](https://github.com/ShiYuPro/project-artifact-cleanup#see-it-work).
The other standalone repositories include first-use commands and their requirements.

## Contributing

Include a realistic failing example, the expected outcome, and the smallest
reproducible input. Keep private logs and credentials out of issues. Improvements
should change a concrete decision or behavior, not add process to every task.

## Sources and license

MIT for the helpers and core skill instructions; CC BY 4.0 for the locale profiles
that adapt Mozilla guidance. Referenced third-party projects and
the separately installed FormatJS packages retain their own licenses. See
[SOURCES.md](SOURCES.md) for reviewed similar skills, decisions, and attribution.

## Creator and contact

[Shiyu Yang](https://github.com/ShiYuPro) · [Apps and portfolio](https://shiu.pro/) · [Contact](https://shiu.pro/contact/)

Open to job opportunities, cofounder conversations, and app or website projects.
