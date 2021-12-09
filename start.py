#!/usr/bin/env python
import sys
import os
from pathlib import Path

q = int(sys.argv[1])
dir = "q" + str(q) + "/"
os.makedirs(dir, exist_ok=True)
Path(dir + "q" + str(q) + "p1.py").touch()
Path(dir + "input.txt").touch()
