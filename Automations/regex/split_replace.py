#!/usr/bin/env python3
import re

re_str = 'One sentence. Another sentence? And last sentence!'

# * Split
# split exclude split values
print(re.split(r'[.?!]', re_str))

# split includes split values
print(re.split(r'([.?!])', re_str))


# We want to split a piece of text by either the word "a" or "the", as implemented in the following code.What is the resulting split list?

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))
#['One sentence. Ano', 'r one? And ', ' l', 'st one!']

# * Sub
re_str1 = 'Received an email for go_nuts95@my.exmaple.com'
print(re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED FROM TEXT]', re_str1))

# Using capturing groups to reverse name
print(re.sub(r'^([\w .-]*), ([\w .-]*)$', r'\2 \1', 'Lovelace, Ada'))
