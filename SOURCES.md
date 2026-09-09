# Sources and second-pass decisions

Reviewed on 2026-09-09 after the initial public-version behavioral tests passed.
Search used GitHub repository/code queries for file-organizer, i18n, deployment,
verification-before-completion and copywriting skills. This is a focused comparison,
not a claim to have reviewed every alternative. Popularity is not adoption evidence
for this repository.

The helpers were generalized from the maintainer's existing local workflows.
The second pass uses the following ideas in our own implementation and wording;
no upstream helper script or complete skill was copied into this release.

| Our skill | Similar skill inspected | License observed | Applied change | Deliberately not adopted |
| --- | --- | --- | --- | --- |
| Project Artifact Cleanup | [deepagentsjs file-organizer](https://github.com/langchain-ai/deepagentsjs/blob/eb859e8b8e2ae533826c6857a2b0745fdd5e357b/examples/skills/file-organizer/SKILL.md) | MIT, LangChain, Inc. | Candidate/deleted payload byte counts; recoverable originals and explicit scope | Whole-home organization, naming conventions, newest-file-wins deletion |
| Evidence-Bound Execution | [Superpowers verification-before-completion](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/verification-before-completion/SKILL.md) | MIT, Jesse Vincent | Bind claims to artifact revision, command/reviewer, environment and observed result | Re-running a full check merely for a new completion message; commands as proof of subjective quality |
| Localize Naturally | [daymade i18n-expert](https://github.com/daymade/claude-code-skills/blob/84fa87b1d6ce0b39291b7ea2778f0c3048a5955b/i18n-expert/SKILL.md) | MIT, daymade | Dynamic-key review, localized error fallbacks and accessibility/non-page surfaces | Assuming English/Chinese are the complete locale set or installing a framework for a wording task |
| Multimodel Chinese Copywriting | [Marketing Skills copywriting](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/copywriting/SKILL.md) | MIT, Corey Haines | Reuse approved context; include evidenced objections, desired reader decision and one next action | Unverified conversion statistics, rigid CTA preferences, invented product proof |
| Fast Deployment Execution | [Vercel deploy-to-vercel](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/deploy-to-vercel/SKILL.md) | Repository license metadata unavailable; no source reuse | Distinguish preview/production and linked account; verify exact returned operation; require post-deploy verification | Automatic linking, broad staging, fallback uploads, copying platform scripts |

MIT license files for the first four repositories were read during this review.
The Vercel skill was consulted for workflow ideas only; an unavailable license is
not permission to redistribute source. The same rule applies to later references.

## Existing localization references

Locale profiles already cited Mozilla, Zulip, Angular, Unicode CLDR, W3C and
language-specific skills before this release. Their per-profile links are retained.
See [attribution and CC BY 4.0 terms](skills/localize-naturally/references/locales/ATTRIBUTION.md).
GitHub metadata confirmed Mozilla's CC BY 4.0, Zulip's Apache-2.0 and Angular's MIT;
no license was identified for w00ing/skills, so its linked skills are not reusable
source material. Registry listings are not proof of original authorship.

## Runtime dependencies

The ICU checker installs `@formatjs/icu-messageformat-parser` 3.5.17 and its
locked dependency `@formatjs/icu-skeleton-parser`. Both package license fields are
MIT. They are installed through `npm ci`; no node_modules files are distributed.
Their package notices remain with installed packages. Python helpers use the
standard library only. Test keys and domains are deliberately fictional.
