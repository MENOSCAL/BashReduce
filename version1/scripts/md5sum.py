#!/usr/bin/python

import hashlib
import sys

m = hashlib.md5()
for line in sys.stdin:
     m.update(line)
     print m.hexdigest()
