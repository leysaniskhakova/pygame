 
import field
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

    def __init__(self, x_size, y_size, x, y):
        self.x_size = x_size
        self.y_size = y_size
        self.left_border = self.x_size[0]
        self.right_border = self.x_size[1]
        self.top_border = self.y_size[1]
        self.bottom_border = self.y_size[0]
        self.x = x
        self.y = y

        self.square = field.Field(self.x_size, self.y_size)

    def render(self):
        self.square.render()

    def start(self): 
        self.x_start = self.x
        self.y_start = self.y
        self.player = Player(self.x_start, self.y_start)
        self.square.field[self.y_start, self.x_start] = '*'

    def player_coordinate(self):
        self.border_check()
        self.player = Player(self.x, self.y)
        if not self.start_coordinate():
            self.square.field[self.y, self.x] = 'И'

    def start_coordinate(self):
        self.border_check()
        if self.square.field[self.y, self.x] == '*':
            return '*'

    def border_check(self):

        if self.x < self.left_border:
            self.x = self.left_border
        elif self.x > self.right_border:
            self.x = self.right_border

        if self.y < self.bottom_border:
            self.y = self.bottom_border
        elif self.y > self.top_border:
            self.y = self.top_border

    def left_step(self):
        if not self.start_coordinate():
            self.square.field[self.y, self.x] = '<'
        self.x = self.player.left()

    def right_step(self):
        if not self.start_coordinate():
            self.square.field[self.y, self.x] = '>'
        self.x = self.player.right()

    def step_up(self):
        if not self.start_coordinate():
            self.square.field[self.y, self.x] = '^'
        self.y = self.player.up()

    def step_down(self):
        if not self.start_coordinate():
            self.square.field[self.y, self.x] = 'v'
        self.y = self.player.down()

    def play(self, action):
        if action == "a":
            self.left_step()
        elif action == "d":
            self.right_step()
        elif action == "w":
            self.step_up()
        elif action == "s":
            self.step_down()
        self.player_coordinate()


def ask_for_action(question):
    response = None
    while response not in ("w", "s", "a", "d", "e"):
        response = input(question).lower()
    return response


def main():
    print("\t\tWelcome!\n")

    x_size = list(map(int, input('Enter the field width (Xmin and Xmax): ').split()))
    y_size = list(map(int, input('Enter the field height (Ymin and Xmax): ').split()))

    x, y = randint(x_size[0], x_size[1]), randint(y_size[0], y_size[1])

    game = Moving(x_size, y_size, x, y)
    game.start()

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
