#!/usr/bin/env python3

import click


@click.command()
@click.option('--greeting', default='Hello', help='Who do you want to greet?')
@click.option('--name', default='Tammy', help='Who do you want to greet?')
def greet(greeting, name):
    print(f"{greeting} {name}")


if __name__ == '__main__':
    greet()
