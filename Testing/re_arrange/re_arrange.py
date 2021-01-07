#!/usr/bin/env python3

import re

# * Define functions


def rearrange_name_regex(name):
    result = re.search(r'^([\w .]*), ([\w .]*)', name)
    # edge case (empty string)
    if result is None:
        return name
    return '{} {}'.format(result[2], result[1])


def rearrange_name(name):
    result = name.split(',')
    return f'{result[1]} {result[0]}'
