import os


def alignment(string, margin):
    return f'{string:{margin}s}\033[0m'

def back_green(string):
    return f'\033[32m\033[42m{string}\033[0m'

def back_purple(string):
    return f'\033[35m\033[45m{string}\033[0m'

def out_purple(string):
    return f'\033[35m{string}\033[0m'

def out_green(string):
    return f'\033[2m\033[32m{string}\033[0m'

def out_blue(string):
    return f'\033[1m\033[34m{string}\033[0m'

def out_red(string):
    return f'\033[1m\033[31m{string}\033[0m'

def out_yellow(string):
    return f'\033[1m\033[33m{string}\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
