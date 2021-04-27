from field import Field
from random import randint

class Player(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self):
        self.x -= 1
        return self.x

    def right(self):
        self.x += 1
        return self.x

    def up(self):
        self.y += 1
        return self.y

    def down(self):
        self.y -= 1
        return self.y

class Moving(object):

    def __init__(self, x_size, y_size):
 
        self.square = Field(x_size, y_size)

        self.x_start = randint(self.square.left_border, self.square.right_border)
        self.y_start = randint(self.square.bottom_border, self.square.top_border)

        self.square[self.y_start, self.x_start] = '*'

        self.player = Player(self.x_start, self.y_start)

    def render(self): 
        self.square.render()

    def start_coordinate(self):
        if self.square[self.player.y, self.player.x] == '*':
            return True
        return False

    def border_check(self):
        if self.player.x < self.square.left_border:
            self.player.x = self.square.left_border
        elif self.player.x > self.square.right_border:
            self.player.x = self.square.right_border
        if self.player.y < self.square.bottom_border:
            self.player.y = self.square.bottom_border
        elif self.player.y > self.square.top_border:
            self.player.y = self.square.top_border

    def player_coordinate(self):
        self.border_check()
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = 'И'

    def step_left(self):
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = '<'
        self.player.left()

    def step_right(self):
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = '>'
        self.player.right()

    def step_up(self):
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = '^'
        self.player.up()

    def step_down(self):
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = 'v'
        self.player.down()

    def play(self, action):
        if action == "a":
            self.step_left()
        elif action == "d":
            self.step_right()
        elif action == "w":
            self.step_up()
        elif action == "s":
            self.step_down()
        self.player_coordinate()

def input_int(text=''):
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            pass

def ask_for_action(question):
    response = None
    while response not in ("w", "s", "a", "d", "e"):
        response = input(question).lower()
    return response

def main():
    print("\t\tWelcome!\n")

    print('Enter the field width:')
    x_min = input_int('Xmin = ')
    x_max = input_int('Xmax = ')

    print('Enter the field width:')
    y_min = input_int('Ymin = ')
    y_max = input_int('Ymax = ')

    game = Moving((x_min, x_max), (y_min, y_max))

    action = None
    while action != "e":
        game.render()
        action = ask_for_action("""
                Which way to take a step?:
                w - step up
                s - step down
                a - step left
                d - step raight
                e - exit
                Enter: """)
        game.play(action)
        print()

print()
main()
