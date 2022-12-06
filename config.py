HOME = '/home/dan'
EDITOR = 'nvim'
TODO_FILE = f'{HOME}/TODO'
CONFIG_DIR = '~/.config/'

configs = {
    'zsh': '~/.zshrc',
    'tmux': '~/.config/tmux/tmux.conf',
    'manage': '~/bin/p/config.py',
    'nvim': '~/.config/nvim/init.vim',
    'alias': '~/.config/aliases',
    'todo': '~/TODO',
    'fastfetch': '~/.config/fastfetch/config.conf',
    'foot': '~/.config/foot/foot.ini',
}

scripts = {
    'rustlings': 'cd ~/p/r/rustlings/ && rustlings list | grep Pending | head -n 1 | awk \'{print $2}\' | xargs lvim',
    'ping': 'echo pong',
    'sync': 'bsync -i ~/Sync klava.wiki:/home/dan/Sync',
}


class Todo:
    box = ['☐', '-']
    done = ['✔', '+']
    cancel = ['✘', 'x']
    symbols = box + done + cancel


# TODO_BOX = ['☐', '-']
# TODO_DONE = ['✔', '+']
# TODO_CANCEL = ['✘', 'x']
# TODO_SYMBOLS = TODO_BOX + TODO_DONE + TODO_CANCEL
