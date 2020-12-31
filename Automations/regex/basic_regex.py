import re

# Starts and ends with 'a'
# works
print(re.search(r'A.*a', 'Argentina'))

# this way it wont matched the whole string
# but it still matches the pattern
print(re.search(r'A.*a', 'Azerbaijan'))

#
