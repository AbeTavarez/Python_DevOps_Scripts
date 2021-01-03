#!/usr/bin/env python3

import re

log = 'January 2 10:30:03 mycomputer bad_process[12345]: Error Performing package upgrade'

regex = r'\[(\d+)\]'
result = re.search(regex, log)

# whole object
print(result)
# list array
print(result[0])
# element
print(result[1])

# will case an Type error if we try to access undefined value
reg_str = '99 elephants in a [cage]'
result_error = re.search(regex, reg_str)
# print(result_error[1])

# function


def extract_pid(log_line):
    regex = r'\[(\d+)\]'
    result = re.search(regex, log_line)

    if result is None:
        return 'No Matches'
    return result[1]


print('Result -->', extract_pid(log))
# will handle Type error and return error message
print('Result -->', extract_pid(reg_str))


# Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.

def extract_pid1(log_line):
    regex = r"\[(\d+)\][:] (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


# 12345 (ERROR)
print(extract_pid1(
    "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
print(extract_pid1("99 elephants in a [cage]"))  # None
print(extract_pid1(
    "A string that also has numbers [34567] but no uppercase message"))  # None
# 67890 (RUNNING)
print(extract_pid1(
    "July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))
