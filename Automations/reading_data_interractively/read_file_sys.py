#!/usr/bin/env python3
"Read Log file and Search for CRON lines"
import sys
import re

if sys.argv[1]:
    logfile = sys.argv[1]
else:
    print('Please include a file path')
    exit(1)

usernames = {}

with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        pattern = r'USER \((\w+)\)$'
        result = re.search(pattern, line)

        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0)+1
        print('Found --->', line.strip())
print(usernames)
