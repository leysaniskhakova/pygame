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

    def __init__(self, square, player):
        self.square = square
        self.player = player

    def render(self): 
        self.square.render()

    def border_check(self):
        if self.player.x < self.square.left_border:
            self.player.x = self.square.left_border
        elif self.player.x > self.square.right_border:
            self.player.x = self.square.right_border
        if self.player.y < self.square.bottom_border:
            self.player.y = self.square.bottom_border 
        elif self.player.y > self.square.top_border:
            self.player.y = self.square.top_border

    def empty_coordinate(self):
        self.square[self.player.y, self.player.x] = '.'

    def player_coordinate(self):
        self.border_check()
        self.square[self.player.y, self.player.x] = 'И'

    def check_obstacles(self, y, x):
        if self.square[y, x] == '#':
            return True
        return False

    def check_step_left(self):
        x_left = self.player.x-1
        if x_left < self.square.left_border:
            x_left = self.square.left_border
        return self.check_obstacles(self.player.y, x_left)

    def check_step_right(self):
        x_right = self.player.x+1
        if x_right > self.square.right_border:
            x_right = self.square.right_border
        return self.check_obstacles(self.player.y, x_right)

    def check_step_up(self):
        y_up = self.player.y+1
        if y_up > self.square.top_border:
            y_up = self.square.top_border
        return self.check_obstacles(y_up, self.player.x)

    def check_step_down(self):
        y_down = self.player.y-1
        if y_down < self.square.bottom_border:
            y_down = self.square.bottom_border
        return self.check_obstacles(y_down, self.player.x)

    def step_left(self):
        if not self.check_step_left():
            self.empty_coordinate()
            self.player.left()
    
    def step_right(self):
        if not self.check_step_right():
            self.empty_coordinate()
            self.player.right()

    def step_up(self):
        if not self.check_step_up():
            self.empty_coordinate()
            self.player.up()

    def step_down(self):
        if not self.check_step_down():
            self.empty_coordinate()
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


def size_x():
    print('Enter the field width:')
    x_min = input_int('Xmin = ')
    x_max = input_int('Xmax = ')
    return x_min, x_max


def size_y():
    print('Enter the field width:')
    y_min = input_int('Ymin = ')
    y_max = input_int('Ymax = ')
    return y_min, y_max


def main():
    print("\t\tWelcome!\n")

    x_size = size_x()
    y_size = size_y()

    square = Field(x_size, y_size)
    player = Player(randint(x_size[0], x_size[1]), randint(y_size[0], y_size[1]))

    game = Moving(square, player)
    game.player_coordinate()

    action = None
    while action != "e":
        game.render()
        action = ask_for_action("""
                Which way to take a step?:
                w - step up
                s - step down
                a - step left
                d - step right
                e - exit
                Enter: """)
        game.play(action)
        print()

print()
main()
