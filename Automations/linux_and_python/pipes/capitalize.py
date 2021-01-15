#!/usr/bin/env python3
import sys

# * We use sys.stdin to read from the standard input

# Loops over each line of file
# that is pass-in  in the stdin
for line in sys.stdin:
    # strips the new line character
    # then capitalize eatch sentence
    print(line.strip().capitalize())


# * We can now re-direct or pipe the context of a file to our capitalize.py script
# * Use:  cat haiku.txt | ./capitalize.py
# * Note you can also use: capitalize.py < haiku.txt
