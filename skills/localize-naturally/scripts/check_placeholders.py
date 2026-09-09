#!/usr/bin/env python3
"""Validate printf arguments or delegate ICU to an actual parser; fail closed."""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

PRINTF = re.compile(
    r"%(?:(?P<position>[1-9]\d*)\$)?(?P<flags>[-+#0 ']*)(?P<width>\d+)?"
    r"(?P<precision>\.\d+)?(?P<length>hh|ll|h|l|L|z|j|t)?(?P<type>[diuoxXfFeEgGaAcsp@])"
)
TEMPLATE = re.compile(r"\{([A-Za-z_][A-Za-z0-9_.-]*)\}")


def placeholders(text: str) -> collections.Counter[str]:
    """Printf contract by runtime argument position, plus escaped percent count."""
    values: list[str] = []
    pos = 0
    implicit = 1
    positional = set()
    while pos < len(text):
        if text[pos] != '%':
            pos += 1
            continue
        if text[pos:pos+2] == '%%':
            values.append('%%')
            pos += 2
            continue
        match = PRINTF.match(text, pos)
        if not match:
            raise ValueError('unrecognized percent syntax; use a project parser for dynamic width/precision, or --syntax plain for literal prose')
        explicit = match.group('position')
        positional.add(bool(explicit))
        slot = int(explicit) if explicit else implicit
        if not explicit:
            implicit += 1
        directive = ''.join(match.group(k) or '' for k in ['flags', 'width', 'precision', 'length', 'type'])
        values.append(f'{slot}:{directive}')
        pos = match.end()
    if len(positional) > 1:
        raise ValueError('mixed indexed and unindexed printf arguments')
    return collections.Counter(values)


def parse_target(raw: str) -> tuple[str, str]:
    if '=' not in raw:
        raise argparse.ArgumentTypeError('target must use LOCALE=TEXT')
    locale, text = raw.split('=', 1)
    if not locale:
        raise argparse.ArgumentTypeError('target locale cannot be empty')
    return locale, text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--source-locale', default='en', help='ICU source grammar locale; set it when source is not English')
    parser.add_argument('--syntax', choices=['auto','printf','icu','template','plain'], default='auto')
    parser.add_argument('--target', action='append', required=True, type=parse_target, metavar='LOCALE=TEXT')
    args = parser.parse_args()
    texts = [args.source] + [text for _, text in args.target]
    syntax = args.syntax
    if syntax == 'auto':
        syntax = 'icu' if any('{' in t or '}' in t for t in texts) else 'printf'
    if syntax == 'plain':
        print('STRUCTURE_NOT_APPLICABLE syntax=plain; no parameter or resource validation claimed')
        return 0
    if syntax == 'icu':
        if any(PRINTF.search(t) for t in texts):
            print('VALIDATION_UNAVAILABLE: mixed ICU/printf requires the project parser', file=sys.stderr)
            return 2
        node = shutil.which('node')
        if not node:
            print('VALIDATION_UNAVAILABLE: Node.js is required for ICU parsing', file=sys.stderr)
            return 2
        try:
            result = subprocess.run([node, str(Path(__file__).with_name('check_icu.mjs'))],
                input=json.dumps({'source':args.source,'sourceLocale':args.source_locale,'targets':args.target}),
                encoding='utf-8', capture_output=True, timeout=20)
        except (OSError, subprocess.TimeoutExpired) as error:
            print(f'VALIDATION_UNAVAILABLE: {error}', file=sys.stderr)
            return 2
        print(result.stdout, end='')
        print(result.stderr, end='', file=sys.stderr)
        return result.returncode
    try:
        def extract(text):
            if syntax == 'template':
                if re.search(r'[{}]', TEMPLATE.sub('', text)):
                    raise ValueError('only simple {name} templates supported; use the actual framework parser')
                return collections.Counter(TEMPLATE.findall(text))
            if '{' in text or '}' in text:
                raise ValueError('brace syntax needs ICU/template or a project parser')
            return placeholders(text)
        expected = extract(args.source)
        failures = []
        for locale, text in args.target:
            actual = extract(text)
            if actual != expected:
                failures.append(f'{locale}: expected={dict(expected)} actual={dict(actual)}')
    except ValueError as error:
        print(f'VALIDATION_UNAVAILABLE: {error}', file=sys.stderr)
        return 2
    if failures:
        print('PLACEHOLDER_MISMATCH', file=sys.stderr)
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print(f'PLACEHOLDER_OK targets={len(args.target)} syntax={syntax} placeholders={dict(expected)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
