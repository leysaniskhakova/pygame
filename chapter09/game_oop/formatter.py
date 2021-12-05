import os


def alignment(string, margin):
    return f'{string:{margin}s}\033[0m'

def bg_green(string):
    return f'\033[32m\033[42m{string}\033[0m'

def bg_purple(string):
    return f'\033[35m\033[45m{string}\033[0m'

def bg_red(string):
    return f'\033[31m\033[41m{string}\033[0m'

def fg_purple(string):
    return f'\033[35m{string}\033[0m'

def fg_green(string):
    return f'\033[2m\033[32m{string}\033[0m'

def fg_blue(string):
    return f'\033[1m\033[34m{string}\033[0m'

def fg_red(string):
    return f'\033[1m\033[31m{string}\033[0m'

def fg_yellow(string):
    return f'\033[1m\033[33m{string}\033[0m'

def fg_faded(string):
    return f'\033[2m{string}\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
