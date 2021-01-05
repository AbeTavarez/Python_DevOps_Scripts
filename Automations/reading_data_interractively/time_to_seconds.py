#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds


cont = 'y'

while (cont.lower() == 'y'):
    hours = int(input('Enter the number of hours: '))
    minutes = int(input('Enter the number of minutes: '))
    seconds = int(input('Enter the number of seconds: '))

    res = to_seconds(hours, minutes, seconds)
    print(f"That's {res} seconds")
    print("-----------------------------------------------")
    cont = input('Do you want to do another conversion? [y to continue]')

print('Good bye :)')
