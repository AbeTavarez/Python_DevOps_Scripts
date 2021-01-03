#!/usr/bin/env python3
import re

# * GROUPS () ()

result = re.search(r'^(\w*), (\w*)$', 'Lovelace, Ada')

print(result)

# Since we use Groups we can now call
print(result.group())  # returns a Tuple

# Using Tuple's indexing
print(result[0])
print(result[1])
print(result[2])
print(f'Her name is {result[2]} and her lastname is {result[1]}')

# * In function


def rearrange_name(name):
    result = re.search(r'^(\w*), (\w*)$', name)

    if result is None:
        return name
    return f'{result[2], result[1]}'


print(rearrange_name('Lovelace, Ada'))
print(rearrange_name('Wayne, Bruce'))

# not match bc of extra space and dot
print(rearrange_name('Hopper, Dennis M.'))

# * Matching middle names, middle initials and double surnames


def rearrange_fullname(name):
    result = re.search(r'^(\w*), (\w*) ?(\w)?(.)?(\w*)$', name)

    result1 = re.search(r'"^([\w \.-]*), ([\w \.-]*)$"', name)

    if result is None:
        return name
    return f'{result[2]} {result[3]}{result[4]} {result[1]}'


print(rearrange_fullname('Kennedy, John F.'))
