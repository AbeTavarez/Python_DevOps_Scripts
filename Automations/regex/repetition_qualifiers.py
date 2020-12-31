# Repetition Qualifiers
import re

# (.*) Any character repeated as many times as possible including 0
print(re.search(r'Py.*n', 'Pygmalion'))  # RETURNS WHOLE WORD

# Being Greedy -> the * takes as many as charaters as possible
print(re.search(r'Py.*n', 'Python Programming'))

# MATCHING JUST ANY LETTERS [a-z]
print(re.search(r'Py[a-z]*n', 'Python Programming'))

#
print(re.search(r'Py[a-z]*n', 'Pyn'))

# (+) SEARCH FOR CHAR REPETIOTIONS (OL) WILL MATCH
print(re.search(r'o+l+', 'goldfish'))
# MATCHING MUTIPLE REPETITIONS
print(re.search(r'o+l+', 'woolly'))
# HERE ARE NO REPETITIONS OF OO OR LL
print(re.search(r'o+l+', 'boil'))

# * Optional
# (?) MARKS THE CHAR FEFORE IT AS "OPTIONAL" MEANING ZERO TO ONE OCCURANCES
print(re.search(r'p?each', 'To each their own'))
# HERE (?) WILL MATCH ONCE
print(re.search(r'p?each', 'I like peaches'))
