#!/usr/bin/env python3
import click

# * Create a top level group


@click.group()
def cli():
  # * func acts as top level group
    pass


@click.group(help='Spawn worker')
def workers():
    worker_name = 'Main worker'


cli.add_command(workers)
