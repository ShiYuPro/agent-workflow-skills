# Message validation boundaries

`scripts/check_placeholders.py` has distinct modes:

- `--syntax auto` routes messages containing braces to the ICU parser; otherwise uses printf validation. Choose explicit syntax for prose/template systems where those characters are literal.
- `--syntax printf` scans escaped `%%` correctly and checks parameter index, conversion, length and formatting options. Indexed target reordering is allowed (`%d %@` → `%2$@ %1$d`). Changing the argument/type association fails. Dynamic `*` widths/precision and unknown dialects return `VALIDATION_UNAVAILABLE`; use the project parser, never report them validated.
- `--syntax icu --source-locale en` uses the pinned `@formatjs/icu-messageformat-parser` (3.5.17). It validates braces, quoting, required `other`, argument types, exact selectors, plural offsets, formatting skeletons and rich-text tag nesting. Target plural categories are checked through the local Node/ICU runtime and may differ from source categories. `=0` is an exact selector, not the same as category `zero`.
- `--syntax template` compares only simple `{name}` parameter counts. It is not ICU, JS template literals, Handlebars, Fluent or markup validation.
- `--syntax plain` explicitly makes no structural validation claim.

ICU setup is local: run `npm ci --ignore-scripts --no-audit --no-fund` in `scripts/` using its committed lockfile if dependencies are missing. Use an allowed cache directory if needed. No strings are sent to a remote translation service; validation reads stdin locally. Missing Node/parser fails with exit 2, never falls back to regex success.

Exit 0 = this mode's structural checks passed; exit 1 = mismatch/invalid ICU; exit 2 = unavailable or unsupported syntax. The exact stdout identifies the mode and ICU runtime version where relevant.

Limits: ICU contract comparison intentionally merges equivalent grammatical-category structures to permit locale-specific plural branches. It does not prove every branch carries equivalent natural-language meaning, that all grammatically useful categories are supplied, or that repeated words/variables are stylistically correct. Review each semantic branch and render realistic quantities. Equal parameter names alone never establish fluency, factual equivalence or native review.

Parse the containing resource separately: iOS `.strings`/`.stringsdict`/`.xcstrings`, Android XML/plurals, JSON, and web ICU/Fluent use different contracts. Do not force ICU syntax onto Swift/Android. Keep full sentences together; preserve meaningful markup and accessibility text. For dates, ranges, units and relative time use the platform formatter rather than hardcoded fragments.

Only deterministic defects block as errors. Label a valid alternative wording as an optional suggestion, and unresolved source or product facts as needing context. No arbitrary native-quality scores.
