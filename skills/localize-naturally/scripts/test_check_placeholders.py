#!/usr/bin/env python3
"""Regression cases for malformed contracts, valid reordering and locale grammar."""
import os
from pathlib import Path
import subprocess
import sys
import unittest

CHECKER = Path(__file__).with_name('check_placeholders.py')

# Expected exit code is part of the public command contract.
CASES = [
 ('printf_same', '%d meals', 'de=%d Mahlzeiten', 0, []),
 ('printf_missing', '%d meals', 'de=Mahlzeiten', 1, []),
 ('printf_wrong_type', '%d meals', 'de=%@ Mahlzeiten', 1, []),
 ('printf_reorder', '%d %@', 'de=%2$@ %1$d', 0, []),
 ('printf_wrong_slots', '%d %@', 'de=%1$@ %2$d', 1, []),
 ('printf_mixed', '%d %@', 'de=%1$d %@', 2, []),
 ('printf_escape', '%%d %d', 'de=%%d %d', 0, []),
 ('printf_escape_lost', '%%d %d', 'de=%d', 1, []),
 ('printf_precision', '%.2f', 'de=%.1f', 1, []),
 ('printf_width_unsupported', '%*d', 'de=%*d', 2, []),
 ('printf_literal_percent', '100%', 'de=100%', 0, ['--syntax','plain']),
 ('template_repeat', '{name} {name}', 'ja={name}', 1, ['--syntax','template']),
 ('template_reorder', '{first} {last}', 'ja={last} {first}', 0, ['--syntax','template']),
 ('template_unknown', '${{name}}', 'ja=${{name}}', 2, ['--syntax','template']),
 ('icu_missing_other', '{count, plural, one {# item} other {# items}}', 'de={count, plural, one {# Element}}', 1, []),
 ('icu_unclosed', '{name}', 'ja={name', 1, []),
 ('icu_argument_type', '{n, number}', 'de={n, date}', 1, []),
 ('icu_exact_selector_lost', '{n, plural, =0 {None} other {# items}}', 'de={n, plural, other {# Elemente}}', 1, []),
 ('icu_offset_changed', '{n, plural, offset:1 other {# items}}', 'de={n, plural, offset:2 other {# Elemente}}', 1, []),
 ('icu_japanese_categories', '{n, plural, one {# item} other {# items}}', 'ja={n, plural, other {#件}}', 0, []),
 ('icu_invalid_ja_category', '{n, plural, one {# item} other {# items}}', 'ja={n, plural, one {#件} other {#件}}', 1, []),
 ('icu_russian_categories', '{n, plural, one {# item} other {# items}}', 'ru={n, plural, one {# запись} few {# записи} many {# записей} other {# записи}}', 0, []),
 ('icu_arabic_categories', '{n, plural, one {# item} other {# items}}', 'ar={n, plural, zero {لا عناصر} one {عنصر واحد} two {عنصران} few {# عناصر} many {# عنصرًا} other {# عنصر}}', 0, []),
 ('icu_select_selector', '{x, select, male {A} other {B}}', 'de={x, select, female {A} other {B}}', 1, []),
 ('icu_tag_removed', '<b>{name}</b>', 'de={name}', 1, ['--syntax','icu']),
 ('icu_tag_nesting', '<b><i>{name}</i></b>', 'de=<i><b>{name}</b></i>', 1, ['--syntax','icu']),
 ('icu_skeleton_changed', '{n, number, ::currency/USD}', 'de={n, number, ::currency/EUR}', 1, []),
 ('icu_quoted_braces', "'{literal}' {name}", "fr='{literal}' {name}", 0, []),
 ('icu_source_locale', '{n, plural, one {# запись} few {# записи} many {# записей} other {# записи}}', 'ja={n, plural, other {#件}}', 0, ['--source-locale','ru']),
 ('icu_mixed_printf', '{name}: %d', 'ja={name}: %d', 2, []),
]

class Regression(unittest.TestCase):
    def test_cli_cases(self):
        for name,source,target,expected,extra in CASES:
            with self.subTest(name=name):
                result=subprocess.run([sys.executable,str(CHECKER),'--source',source,'--target',target,*extra],capture_output=True,text=True,timeout=25)
                self.assertEqual(result.returncode,expected,result.stdout+result.stderr)
                if expected:
                    self.assertNotIn('_OK ',result.stdout)

    def test_missing_node_fails_closed(self):
        result=subprocess.run([sys.executable,str(CHECKER),'--source','{name}','--target','ja={name}'],env={**os.environ,'PATH':''},capture_output=True,text=True)
        self.assertEqual(result.returncode,2)
        self.assertIn('VALIDATION_UNAVAILABLE',result.stderr)

if __name__ == '__main__':
    unittest.main()
