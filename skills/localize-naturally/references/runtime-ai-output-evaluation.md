# Runtime AI localization evaluation

Use this reference when an app, website, support flow, agent, or model generates user-visible localized text at runtime.

## Define the claim before testing

Choose the narrowest honest claim:

- `language compliant`: output uses the requested language and region.
- `terminology compliant`: required names and domain terms follow the approved glossary.
- `locally natural`: wording is normal for the target audience and surface.
- `native reviewed`: a qualified native reviewer actually reviewed the covered outputs.

Never infer the last claim from an LLM judge, translation API, character-set check, or one fluent-looking sample.

## Build a representative set

Stratify cases by locale, surface, intent, length, ambiguity, and risk. Include:

- common inputs and long-tail terminology;
- unclear, incomplete, noisy, or adversarial inputs;
- names and loanwords that should remain stable;
- numbers, units, dates, prices, negation, and confidence qualifiers;
- layouts or scripts likely to expose mixed-language output;
- prior production failures and real user corrections.

Keep source material, expected meaning, accepted local terms, rejected forms, and review status with each case.

## Sample repeated outputs

- Use identical inputs across providers or prompt versions.
- Record provider, model, prompt version, locale, temperature, image/text preprocessing, and timestamp.
- Repeat the high-variance or high-risk subset at least three times even when temperature is zero.
- Do not silently retry away malformed, wrong-language, or unsafe responses; count the first failure and record any recovery separately.

## Score distinct failure classes

Keep separate binary or countable fields for:

1. requested language and regional variant;
2. meaning and factual invariants;
3. approved terminology or established local name;
4. mixed-language leakage and wrong writing system;
5. literal, invented, awkward, or generic wording;
6. confidence or safety meaning changed;
7. placeholders, markup, JSON, or schema preserved;
8. layout or interaction fit when applicable.

Do not replace these with one opaque quality score. A global average must always be accompanied by per-locale results and raw failure examples.

For image recognition, retrieval, or other benchmark tasks, also keep three evaluation layers separate:

1. `ground-truth quality`: whether the test asset actually supports the reference label and accepted aliases;
2. `task accuracy`: whether the model identified what is visibly present at an appropriate level of specificity;
3. `language quality`: whether the correct or appropriately broad result is expressed naturally in the requested locale.

Quarantine disputed or mislabeled assets before publishing accuracy or localization rates. Record every ground-truth correction with the original label, revised label, reason, and reviewer evidence. Never change a label merely to match one provider's output.

## Use automation carefully

Deterministic checks are suitable for placeholders, schema, forbidden terms, duplicate text, obvious script mismatch, mixed-language fragments, numbers, units, and required terminology.

LLM judging may prioritize outputs for review, but it must not be the only judge of its own language quality. Calibrate automated judgments against a reviewed subset and preserve disagreements.

Human review is required before claiming native quality, especially for unfamiliar locales, legal/health/financial text, culturally sensitive wording, or recurring borderline cases.

## Decide what to fix

- Fix the prompt when failures share a general instruction or context gap.
- Fix the glossary or accepted-name table when terminology is missing or ambiguous.
- Use deterministic post-processing only for schema and other true invariants.
- Route to confirmation or a broader name when evidence cannot support a precise localized term.
- Prefer targeted locale guidance over copying every locale's rules into every request.

Re-run the affected slice and a broad regression set after each change. Do not tune against one image, sentence, or random output.

## Report honestly

State the number of unique cases and total generations, the repeated subset, providers and models, locale distribution, pass/failure counts, review method, unresolved locales, and whether testing covered source files, a harness, real runtime traffic, or production.
