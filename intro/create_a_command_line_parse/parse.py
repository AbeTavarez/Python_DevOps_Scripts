#!/usr/bin/env python3

# * Getting arguments from the terminal in a vanilla way(no modules).


# We need the sys module
import sys


def user_greeting(greeting, name):
    message = f'{greeting} {name}'
    print(message)


# The expression (if __name__ == '__main__':) will test if we are running the script from the terminal.


if __name__ == '__main__':
    greeting = 'Hello'
    name = 'User'

    if '--help' in sys.argv:
        help_message = f'Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>'
        print(help_message)
        sys.exit()

    if '--name' in sys.argv:
        # get position after name flag
        name_index = sys.argv.index('--name') + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if '--greeting' in sys.argv:
        # get position after greeting flag
        greeting_index = sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

user_greeting(greeting, name)

# * First make the script executable
# * Now you can run the script:
# ./parse.py --greeting 'Welcome to the Matrix' --name "Neo"
