# Setup and first checks

Python 3.9+ handles printf and simple template checks with the standard library.
ICU checks also require Node.js 20+ with full ICU and the pinned parser:

```sh
cd skills/localize-naturally/scripts
npm ci --ignore-scripts
python3 check_placeholders.py --source 'Remaining: %d' --target 'fr=Restant : %d'
python3 check_placeholders.py --source 'Remaining: %d' --target 'fr=Restant : %s'
```

The first command should pass; the second must fail because the argument type changed.
Run `python3 -m unittest discover -s . -p 'test_*.py'` from this scripts directory.
The locale profiles are starting points, not native-speaker certification. ExampleApp
is a fictional brand used by the evaluation fixtures. Add project locales as needed.
Missing Node/parser is an unavailable validation, never a pass.
