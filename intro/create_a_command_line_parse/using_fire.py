#!/usr/bin/env python3

import fire


def greet(greeting='hey', name='abe'):
    print(f"{greeting} {name}")


if __name__ == '__main__':
    fire.Fire()
