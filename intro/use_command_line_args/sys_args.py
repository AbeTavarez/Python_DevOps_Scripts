#!/usr/bin/env python3

# *********** First command line tool ************

# import the system module
import sys

# we can pass a List of arguments to our script when we're executing it from the command line or terminal

# This Argument List is called 'argv' or 'arguments vertor'

# Let's se this in action:

if __name__ == "__main__":
    print(f'The first argument -> : {sys.argv[0]}')
    print(f'The second argument -> : {sys.argv[1]}')
    print(f'The third argument -> : {sys.argv[2]}')
    print(f'The fourth argument -> : {sys.argv[3]}')


# * Now run the script from the command line with the fillowing arguments:
# * Rememmber you need to be in the same directory the script is located
# ./sys_args.py 'arg1' 'arg2' 'arg3'
