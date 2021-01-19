#!/usr/bin/env python3

# * Using Argparse module to handle command line arguments

import argparse

if __name__ == '__main__':
    # Create parser object with it's documentation
    parser = argparse.ArgumentParser(description='Echo input')
    # adds position based command with it's help message
    parser.add_argument('message', help='Message to echo')
    # adds optional argument, storing it as a boolean
    parser.add_argument('--twice', '-t', help='Do it twice',
                        action='store_true')
    # Use the parser to parse the arguments
    args = parser.parse_args()
    # Now we have access the arguments value by their names
    print(args.message)
    # the (--) is removed from (--twice)
    if args.twice:
        print(args.message)


# * Now you can execute this script with:
#   ./using_argparse.py hello there!
#   ./using_argparse.py hello there! --twice
