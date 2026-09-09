# Natural localization review patterns

Use this reference for translation audits, unfamiliar locales, or high-risk copy.

## Diagnose before rewriting

For each questionable string, record:

1. Intended user outcome.
2. Facts and obligations that cannot change.
3. Surface and available space.
4. Target audience and regional variant.
5. Project-approved terminology.
6. Risk if the wording is misunderstood.

## Common failure patterns

| Signal | Why it fails | Better response |
| --- | --- | --- |
| The target keeps source-language word order | It reads as translated even when every word is correct | Rebuild the sentence around normal target-language information order |
| A dictionary chooses the wrong domain meaning | Words such as `private`, `lot`, `condition`, or `consignment` are highly contextual | Choose the established product or industry term from the project glossary |
| A phrase repeats, such as `private private` | Translation passes structural checks but exposes machine assembly | Remove duplication and rewrite the whole phrase naturally |
| Every sentence starts with the product name | Copy sounds generated and promotional | Use local cohesion and omit repeated subjects where natural |
| Long labels are solved only by shrinking type | Readability drops and the layout remains fragile | Shorten the label first; keep the action and result |
| Legal language becomes more definite | Smooth wording silently changes responsibility | Restore qualifiers and flag missing legal facts |
| Marketing translation adds superlatives | Localizer invents evidence or investment claims | Preserve the source confidence and use verifiable facts only |
| Locale files are complete but the page overflows | Structural completeness is not user experience | Verify long words, narrow screens, RTL, and mixed numerals in the real UI |
| Review approval becomes "live" or "available to download" | A smoother sentence invents a later lifecycle state | Name only the state supported by evidence and keep later states separate |
| A previously rejected term returns in a later revision | Local optimization overrides an explicit project decision | Search task and project decisions first; follow the latest explicit correction |
| A placeholder is translated by guessed meaning | `%d` or an ICU argument may represent a different quantity at runtime | Preserve identity and type; verify the complete message and plural branches |
| A self-check says the state is accurate but the draft says "live" or "download now" | The summary is trusted instead of the delivered body | Scan the actual draft against the currently verified lifecycle state |
| A generated cache replaces existing locale files | Newer output is treated as more authoritative than approved copy | Diff first; fill reviewed gaps only and preserve authoritative non-empty translations |
| App resources are complete but store metadata is missing | Separate localization surfaces are collapsed into one completion claim | Inventory app, permission, store, screenshot, server, and runtime surfaces independently |

## Contrast examples

These examples illustrate method, not universal approved wording.

- Wrong domain: German `Private` translated as `Gefreiter`.
  - Diagnose the context first. A private-sale service needs `privat`, `Privatverkauf`, or `private Beratung`, not a military rank.
- Machine assembly: `Private private Beratung`.
  - Rewrite the phrase as one local concept, such as `Private Beratung`.
- Literal product instruction: “Click here to view the product page.”
  - Use the local action the user wants, such as “View product” or its natural local equivalent.
- Overclaim: “A must-have with strong appreciation potential.”
  - Retain only documented facts. Do not translate an unsupported investment promise into smoother sales language.
- Layout failure: a compact source button expands into a sentence.
  - Keep the core action, move explanation into nearby body copy, and preserve the control skeleton.
- Language selector failure: `Japanese` or `Korean` becomes a demonym such as "Japanese person" or "Korean person".
  - Use the language's approved display label or native label. Keep stored locale codes separate from visible labels, and use `translate=no` where automatic page translation must not rewrite the selector.

## Review sequence

1. Meaning and factual equivalence.
2. Terminology and local register.
3. Naturalness and concision.
4. Numbers, negation, placeholders, and markup.
5. Layout, RTL, accessibility, and navigation.
6. Legal or specialist escalation.

Passing later checks never compensates for a failure in meaning or factual equivalence.
