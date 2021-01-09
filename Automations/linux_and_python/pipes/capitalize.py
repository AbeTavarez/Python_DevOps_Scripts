#!/usr/bin/env python3
import sys

# loops over each line of file
# that is pass in  as stdin
for line in sys.stdin:
    # strips the new line character
    # then capitalize eatch sentence
    print(line.strip().capitalize())
