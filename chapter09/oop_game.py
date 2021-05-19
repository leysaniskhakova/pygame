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

    def get_player_coordinate(self):
        return self.y, self.x

class Moving(object):

    def __init__(self, x_size, y_size):
 
        self.square = Field(x_size, y_size)

        self.x_start = randint(self.square.left_border+1, self.square.right_border-1)
        self.y_start = randint(self.square.bottom_border+1, self.square.top_border-1)

        self.square[self.y_start, self.x_start] = '*'

        self.player = Player(self.x_start, self.y_start)

    def render(self): 
        self.square.render()

    def start_coordinate(self):
        if self.square[self.player.y, self.player.x] == '*':
            return True
        return False

    def border_check(self):
        if self.player.x < self.square.left_border+1:
            self.player.x = self.square.left_border+1
        elif self.player.x > self.square.right_border-1:
            self.player.x = self.square.right_border-1
        if self.player.y < self.square.bottom_border+1:
            self.player.y = self.square.bottom_border+1
        elif self.player.y > self.square.top_border-1:
            self.player.y = self.square.top_border -1

    def exit_check(self):
        if self.player.get_player_coordinate() != self.square.exit_coordinate():
            self.border_check()
            self.player_symbol()
            return True
        else:
            return False

    def player_symbol(self):
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

        self.exit_check()


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

    action = None

    x, y = 1, 5
    while y <= 11:
        
        game = Moving(*[(x, y), (x, y)])

        while game.exit_check() and action != 'e':
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

        if action == 'e':
            print('Come back!')
            break
        elif y == 8 or y == 5:
            print('Next level!')
        elif y == 11:
            print('You have found a way out!')
        y += 3

print()
main()
