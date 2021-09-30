import formatter


def input_int(parameter, text=''):
    while True:
        print(f'{parameter}: ', end='')
        try:
            number = int(input(text))
            if number > 0:
                return number
            else:
                print(formatter.fg_red('\nThe number must be positive!'))
        except ValueError:
            print(formatter.fg_red('\nEnter the number!'))
            pass


def first_level():
    print(formatter.fg_green('\nEnter the size of the first playing field (number of cells in height and width):'))
    return input_int(formatter.fg_blue('\nwidth')), input_int(formatter.fg_blue('\nheight'))


def next_level():
    print(formatter.fg_green('\nSelect how many cells the next field will be larger than the previous one'))
    return input_int(formatter.fg_blue('\nrise'))


def last_level():
    print(formatter.fg_green('\nEnter the number of levels'))
    return input_int(formatter.fg_blue('\nlevels'))


def ask_for_action(question):
    response = None
    while response not in ("w", "s", "a", "d", "e"):
        response = input(question).lower()
    return response


def input_data():
    level_fields = {}
    start = 1
    width, height = first_level()
    rise, levels = next_level(), last_level()

    for level in range(1, levels+1):
        level_fields[level] = [(start, width), (start, height)]
        width += rise
        height += rise
    
    return level_fields


def step_question():
    return """
Which way to take a step?:
w - step up
s - step down
a - step left
d - step raight
e - exit
Enter: """


def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    if response == "y":
      return True
    elif response == "n":
      return False 


def message(text):
    print(formatter.fg_red(f'{text}'))
    input(formatter.fg_yellow("(press 'enter' to proceed)"))
