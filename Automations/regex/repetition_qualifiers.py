# Repetition Qualifiers
import re

# (.*) Any character repeated as many times as possible including 0
print(re.search(r'Py.*n', 'Pygmalion'))

# Being Greedy -> the * takes as many as charaters as possible
print(re.search(r'Py.*n', 'Python Programming'))

#
print(re.search(r'Py[a-z]*n', 'Python Programming'))

#
print(re.search(r'Py[a-z]*n', 'Pyn'))

# + letter repetition
print(re.search(r'o+l+', 'goldfish'))
print(re.search(r'o+l+', 'woolly'))
# somthing that doest'n match
print(re.search(r'o+l+', 'boil'))

# * Optional
#not included
print(re.search(r'p?each', 'To each their own'))
# included
print(re.search(r'p?each', 'I like peaches'))
