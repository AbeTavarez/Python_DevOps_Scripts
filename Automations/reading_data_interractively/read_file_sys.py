#!/usr/bin/env python3

import sys

if sys.argv[1]:
    logfile = sys.argv[1]
else:
    exit(1)
with open(logfile) as f:
    for line in f:
        print(line.strip())
