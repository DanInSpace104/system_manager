import os
from pprint import pprint as pp

import click

import config as c
from click_aliased_group import AliasedGroup
from config import Todo


def indent(string: str):
    return len(string[: -len(string.lstrip())])


def open_todos() -> str:
    with open(c.TODO_FILE) as f:
        content = f.read()
    return content


def load_recursive(lines):
    pass


def load_todos(content: str) -> dict:
    '''
    # PyParsing?
    '''
    res = {}
    state = 'project'
    project = 'Inbox'
    lines = []
    for line in content.splitlines():
        lines.append([indent(line), line.strip(), []])

    prev_line = lines[0]
    for l in lines:
        if l[0] > prev_line[0]:
            prev_line.append(l)
        print(prev_line)

    pp(lines)


@click.group(cls=AliasedGroup)
@click.option('--project', '-p', default='Inbox')
@click.pass_context
def todo(ctx, project):
    ctx.obj['debug'] and print(f'{project=}')
    ctx.ensure_object(dict)


@todo.command()
@click.option('--all', '-a', is_flag=True, default=False)
@click.pass_context
def list_todo(ctx, all):
    # print(open_todos())
    load_todos(open_todos())


@todo.command()
def edit():
    file = c.configs['todo']
    os.system(f'{c.EDITOR} {file}')


if __name__ == '__main__':
    todo()
