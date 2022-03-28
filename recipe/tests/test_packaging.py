#!/usr/bin/env python

from pathlib import Path
import sys

import cylc.uiserver


def check_path(path):
    package_path = Path(cylc.uiserver.__file__).parent / path
    if not package_path.exists():
        raise Exception(f'Path does not exist: {package_path}')
    print(f'Path found in: {package_path}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Only one argument accepted')
    check_path(sys.argv[1])
