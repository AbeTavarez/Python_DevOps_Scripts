#!/usr/bin/env/ python3

# * Using Argparse module to handle command line arguments

import argparse

if __name__ == '__main__':
    # Create parser object with it's documentation
    parser = argparse.ArgumentParser(description='Echo input')
    # adds position based command with it's help message
    parser.add_argument('message', help='Message to echo')

    parser.add_argument('--twice', '-t', help='Do it twice',
                        action='store_true')

    args = parser.parse_args()

    print(args.message)

    if args.twice:
        print(args.message)
