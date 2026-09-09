// Parse actual ICU syntax; argument-name regexes cannot validate branches or quoting.
import {readFileSync} from 'node:fs';

let parse;
try {
  ({parse} = await import('@formatjs/icu-messageformat-parser'));
} catch {
  console.error('VALIDATION_UNAVAILABLE: ICU parser missing; run npm ci --ignore-scripts in this scripts directory');
  process.exit(2);
}

const stable = value => JSON.stringify(value);
const sorted = items => [...new Set(items)].sort();
function style(value) {
  if (!value || typeof value === 'string') return value ?? null;
  // Location metadata is irrelevant; preserve the actual number/date skeleton.
  if (value.tokens) return {type: value.type, tokens: value.tokens};
  return {type: value.type, pattern: value.pattern};
}

function contract(nodes, locale, prefix = '') {
  const result = [];
  for (const n of nodes) {
    if (n.type === 0) continue; // Literal wording belongs to language review.
    if (n.type === 7) {result.push(prefix + '#'); continue;}
    if (n.type === 8) {
      result.push(prefix + 'tag:' + n.value);
      result.push(...contract(n.children, locale, prefix + 'tag:' + n.value + '/'));
      continue;
    }
    result.push(prefix + stable({name: n.value, type: n.type, style: style(n.style)}));
    if (n.type !== 5 && n.type !== 6) continue;
    const selectors = Object.keys(n.options);
    if (n.type === 6) {
      const categories = new Intl.PluralRules(locale, {type: n.pluralType}).resolvedOptions().pluralCategories;
      for (const key of selectors) {
        if (!key.startsWith('=') && !categories.includes(key)) {
          throw new Error(`${locale}: invalid ${n.pluralType} category ${key}`);
        }
      }
      result.push(prefix + stable({plural: n.value, kind: n.pluralType, offset: n.offset,
        exact: selectors.filter(x => x.startsWith('=')).sort()}));
      for (const key of selectors) {
        // Locale categories may differ. Preserve structure inside exact branches,
        // and the union of contracts inside grammatical branches, not their counts.
        const branch = key.startsWith('=') ? key : 'category';
        result.push(...contract(n.options[key].value, locale, prefix + n.value + '/' + branch + '/'));
      }
    } else {
      result.push(prefix + stable({select: n.value, selectors: selectors.sort()}));
      for (const key of selectors) {
        result.push(...contract(n.options[key].value, locale, prefix + n.value + '/' + key + '/'));
      }
    }
  }
  return sorted(result);
}

function checkLocale(locale) {
  if (!Intl.PluralRules.supportedLocalesOf([locale]).length) {
    throw new Error(`Locale not supported by this Node/ICU runtime: ${locale}`);
  }
}

try {
  const data = JSON.parse(readFileSync(0, 'utf8'));
  checkLocale(data.sourceLocale);
  const options = {requiresOtherClause: true, captureLocation: false};
  const source = contract(parse(data.source, options), data.sourceLocale);
  for (const [locale, text] of data.targets) {
    checkLocale(locale);
    const target = contract(parse(text, options), locale);
    if (stable(source) !== stable(target)) {
      throw new Error(`${locale}: argument/type/tag/selector/skeleton contract changed`);
    }
  }
  console.log(`ICU_OK targets=${data.targets.length} parser=3.5.17 node=${process.versions.node} icu=${process.versions.icu}`);
} catch (error) {
  console.error(`ICU_INVALID: ${error.message}`);
  process.exit(1);
}
