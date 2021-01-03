#!/usr/bin/env python3
import re

re_str = 'One sentence. Another sentence? And last sentence!'

# * Split
# split exclude split values
print(re.split(r'[.?!]', re_str))

# split includes split values
print(re.split(r'([.?!])', re_str))

# * Sub
re_str1 = 'Received an email for go_nuts95@my.exmaple.com'
print(re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED FROM TEXT]', re_str1))
