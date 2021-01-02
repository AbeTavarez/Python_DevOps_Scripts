import re

# Name of country start and ends with A a
print(re.search(r'A.*a', 'Argentina'))

# This will also match the following country
print(re.search(r'A.*a', 'Azerbaijan'))

# We need to make our pattern strictier
# Adding (^ $) makes sure we only get matching that beggins and ends with A a in this case
# Should not match now
print(re.search(r'^A.*a$', 'Azerbaijan'))

# But still work for
print(re.search(r'^A.*a$', 'Australia'))

# * Checks if variable name is valid

# Pattern Desc
# 1- can only start with letters or underscore
# 2- Can contain letters, numbers and underscores till end of pattern
pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

print(re.search(pattern, '_valid_name'))  # ok
print(re.search(pattern, 'no spaces allowed'))  # nop
print(re.search(pattern, 'my_var1'))  # ok
print(re.search(pattern, '1my_var'))  # nop
