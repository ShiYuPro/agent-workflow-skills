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

Start with **[Project Artifact Cleanup](skills/project-artifact-cleanup/SKILL.md)**
if your agent keeps leaving screenshots, experiments, logs, and outdated drafts
around your project. It manages only artifacts you deliberately enroll. It does
not guess which source files are safe to delete.

| Skill | Use it when | Included tooling |
| --- | --- | --- |
| [Project Artifact Cleanup](skills/project-artifact-cleanup/SKILL.md) | Agent scratch and review files keep accumulating | Preview, retention, pinning, recovery before expiry, guarded sweep |
| [Localize Naturally](skills/localize-naturally/SKILL.md) | UI translations lose meaning, placeholders, or layout fit | printf/template and ICU checks; 12 starter locale profiles |
| [Evidence-Bound Execution](skills/evidence-bound-execution/SKILL.md) | Requirements are acknowledged but disappear from the result | Lightweight execution card; optional versioned evidence gate |
| [Multimodel Chinese Copywriting](skills/multimodel-chinese-copywriting/SKILL.md) | You want an external Chinese model to draft and an agent to verify | Explicit provider configuration, offline dry run, no automatic retries |
| [Fast Deployment Execution](skills/fast-deployment-execution/SKILL.md) | Release work repeats checks without reaching a verified result | Optional timed command runner; project-owned release procedure |

## Install only what you need

Clone or download this repository, then copy one skill into your agent's skill
directory. From the repository root, for Codex in an existing project:

```sh
python3 scripts/install.py project-artifact-cleanup --dest /path/to/project/.agents/skills
```

For Claude Code, use `/path/to/project/.claude/skills` instead. A global installation
can target your agent's documented user skill directory. The installer refuses
existing skill destinations and omits dependencies and generated caches. It does
not alter project instructions, schedule tasks, or install packages.

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

See [first-use commands and policy setup](skills/project-artifact-cleanup/references/setup.md).
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

```sh
python3 skills/multimodel-chinese-copywriting/scripts/multimodel_copywriting.py --provider kimi --prompt-file examples/copy-brief.txt --dry-run
python3 skills/localize-naturally/scripts/check_placeholders.py --source 'Remaining: %d' --target 'fr=Restant : %d'
python3 scripts/check.py
```

Install the ICU dependency before the full check. Tests use temporary directories
and mocked provider responses; they do not call paid APIs, deploy services, or
clean your projects. Tests establish scripted behavior, not native-speaker quality,
real provider availability, user adoption, or production readiness of a release.

## Contributing

Include a realistic failing example, the expected outcome, and the smallest
reproducible input. Keep private logs and credentials out of issues. Improvements
should change a concrete decision or behavior, not add process to every task.

## Sources and license

MIT for the helpers and core skill instructions; CC BY 4.0 for the locale profiles
that adapt Mozilla guidance. Referenced third-party projects and
the separately installed FormatJS packages retain their own licenses. See
[SOURCES.md](SOURCES.md) for reviewed similar skills, decisions, and attribution.
