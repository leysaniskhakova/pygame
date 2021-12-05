import formatter


def input_int(parameter):
    while True:
        print(f'{parameter}: ', end='')
        try:
            number = int(input())
            if number > 0:
                return number
            else:
                print(formatter.fg_red('\nThe number must be positive!'))
        except ValueError:
            print(formatter.fg_red('\nEnter the number!'))
            pass


def first_field_size():
    print(formatter.fg_green('\nEnter the size of the first playing field (number of cells in height and width):'))
    return input_int(formatter.fg_blue('\nwidth')), input_int(formatter.fg_blue('\nheight'))


def field_increase():
    print(formatter.fg_green('\nSelect how many cells the next field will be larger than the previous one'))
    return input_int(formatter.fg_blue('\nrise'))


def number_of_levels():
    print(formatter.fg_green('\nEnter the number of levels'))
    return input_int(formatter.fg_blue('\nlevels'))


def ask_for_action(question):
    response = None
    while response not in ("w", "s", "a", "d", "e"):
        response = input(question).lower()
    return response


def input_data():
    level_fields = {}
    width, height = first_field_size()
    rise, levels = field_increase(), number_of_levels()

    for level in range(1, levels+1):
        level_fields[level] = [width, height]
        width += rise
        height += rise
    
    return level_fields

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question + ' (y/n)\n').lower()
    if response == "y":
      return True
    elif response == "n":
      return False 


def print_yellow_text(text):
    print(formatter.fg_yellow(text))

def string_level(level):
    return f'\t\tlevel {level} \n'

def string_energy_units(energy_units):
    return f'\t energy units: {energy_units} \n'

def print_blue_text(text):
    print(formatter.fg_blue(text))

def print_red_text(text):
    print(formatter.fg_red(text))

def message(text):
    print_red_text(text)
    input("(press 'enter' to proceed)")
    