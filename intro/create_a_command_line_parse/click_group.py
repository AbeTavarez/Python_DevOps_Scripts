#!/usr/bin/env python3
import click

# * Create a top level group


@click.group()
def cli():
  # * func acts as top level group
    pass


@click.group(help='Worker related commands')
def workers():
  # * Create a group to to hold the workers commands
    pass


# * Adds the workers group as a command to top level group
cli.add_command(workers)


@workers.group(help='Spawn new worker')
def worker():
    worker_name = 'Main worker'
    print(f"{worker_name} is now spawing...")


@workers.command(help='List all of the workers')
def list_workers():
    workers_list = ['alpha', 'bravo', 'charlie']
    print(f"Workers: {','.join(workers_list)}")


@cli.command(help='Talk to worker')
@click.option('--greeting', default='Whats up bro?', help='Greating from admin')
@click.argument('name')
def admins(greeting, name):
    message = f'{greeting} {name}'
    print(message)


if __name__ == '__main__':
    cli()
