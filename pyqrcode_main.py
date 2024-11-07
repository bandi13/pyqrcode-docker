#!/usr/bin/env python3
import sys
import os
import pyqrcode

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: pyqrcode_main.py <argument>")
        sys.exit(1)

    error=os.environ['PYQRCODE_ERROR']
    version=os.environ['PYQRCODE_VERSION']
    if version == '':
        version = None
    else:
        version = int(version)
    mode=os.environ['PYQRCODE_MODE']
    if mode == '':
        mode = None
    qr = pyqrcode.create(sys.argv[1], error=error, version=version, mode=mode)
    print(qr.terminal(os.environ['PYQRCODE_FGCOLOR'],os.environ['PYQRCODE_BGCOLOR']))
    qr.png('pyqrcode.png', scale=5)
