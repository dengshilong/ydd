# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Time    : 17/2/6 下午5:31
# @Author  : robinjia
# @Email   : dengshilong1988@gmail.com
import click
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
