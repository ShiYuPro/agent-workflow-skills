#!/usr/bin/env python3
"""Copy one skill into an explicitly selected directory, without overwriting."""
import argparse
import shutil
from pathlib import Path


def main():
    source_root = Path(__file__).resolve().parents[1] / 'skills'
    names = sorted(p.name for p in source_root.iterdir() if (p / 'SKILL.md').is_file())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill', choices=names)
    parser.add_argument('--dest', type=Path, required=True)
    args = parser.parse_args()
    source = source_root / args.skill
    target = args.dest.expanduser().resolve() / args.skill
    if target.exists() or target.is_symlink():
        parser.error('Destination skill exists; compare versions before replacing it')
    if source == target or source in target.parents:
        parser.error('Destination must be outside the source skill')
    for file in source.rglob('*'):
        if file.is_symlink():
            parser.error('Source contains a symlink; inspect before installing')
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns('node_modules', '__pycache__', '*.pyc', '.DS_Store'))
    print(target)


if __name__ == '__main__':
    main()
