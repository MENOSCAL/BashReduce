#!/usr/bin/env python

import hashlib
import sys

h = hashlib.sha1()

for line in sys.stdin:
     h.update(line)
     print h.hexdigest()
