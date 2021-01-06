import re


def show_time_of_pid(line):
    # how to do it in one group?
    pattern = r'^([A-Za-z]+ \d \d+:\d+:\d+)'
    result = re.search(pattern, line)
    p2 = r'(\d{5})'
    r2 = re.search(p2, line)
    return '{} pid:{}'.format(result[1], r2[1]) pattern = r'^([A-Za-z]+ \d \d+:\d+:\d+)'


# pattern = r'^([A-Za-z]+ \d \d+:\d+:\d+) (\[\d+\])'
# result = re.search(pattern, line)
# print(type(result))
# return f'{result[1]}'

# When searching log files using regex, which regex statement will search for the alphanumeric word "IP" followed by one or more digits wrapped in parentheses using a capturing group?
#r"IP \((\d+)\)$"

#
# Jul 6 14:01:23 pid:29440
print(show_time_of_pid(
    "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))

# Jul 6 14:02:08 pid:29187
print(show_time_of_pid(
    "Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))

# Jul 6 14:02:09 pid:29187
print(show_time_of_pid(
    "Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"))

# Jul 6 14:03:01 pid:29440
print(show_time_of_pid(
    "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"))

# Jul 6 14:03:40 pid:29807
print(show_time_of_pid(
    "Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))

# Jul 6 14:04:01 pid:29440
print(show_time_of_pid(
    "Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"))

# Jul 6 14:05:01 pid:29440
print(show_time_of_pid(
    "Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"))
