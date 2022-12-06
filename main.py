import os
from pprint import pprint

import click

import config as c
from click_aliased_group import AliasedGroup
from todo import todo


def print_script_names():
    pprint([s for s in c.scripts])


@click.group(cls=AliasedGroup)
@click.option('--debug', '-D', is_flag=True, default=False)
@click.pass_context
def main(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj['debug'] = debug


@main.command()
@click.argument('entity')
@click.pass_context
def config(ctx, entity):
    file = c.configs.get(entity, c.CONFIG_DIR + entity)
    if ctx.obj['debug']:
        print(f'{c.EDITOR=} {file=}')
    else:
        os.system(f'{c.EDITOR} {file}')


@main.command(help='Send to ReadLater channel')
@click.argument('string', nargs=-1)
@click.pass_context
def readlater(_, string):
    os.system(f'telegram-send {" ".join(string)}')


@main.command()
@click.argument('name', default='')
@click.option('-l', '--list', is_flag=True, help='Print avaliable script names')
@click.pass_context
def run(ctx, name, list):
    if list:
        print_script_names()
        return
    script = c.scripts.get(name)
    if not script:
        print(f'script {name} is not found')
        return
    if ctx.obj['debug']:
        print(script)
    else:
        os.system(script)


main.add_command(todo)

if __name__ == '__main__':
    main()
