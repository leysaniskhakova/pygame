from field import Field
from player import Player
from random import randint


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

    def player_coordinate(self):
        self.border_check()
        self.square[self.player.y, self.player.x] = 'И'

    def check_energy(self, y, x):
        if self.square.has_energy(y, x):
            self.player.energy_increased()

    def check_obstacle(self, y, x):
        if not self.square.has_obstacle(y, x):
            return True
        return self.ask_about_annihilation() and self.annihilation()

    def ask_about_annihilation(self):
        return ask_yes_no('Destroy an obstacle for 10 energy units? (y/n)\n')

    def annihilation(self):
        if self.player.level_energy() > 0:
            self.player.energy_decreased()
            return True
        else:
            print('Lack of energy!')
            return False

    def step(self, y, x):
        self.check_energy(y, x)
        self.square.reset_old_position(self.player.y, self.player.x)

    def step_left(self):
        x_left = self.player.x-1
        if x_left < self.square.left_border:
            x_left = self.square.left_border

        if self.check_obstacle(self.player.y, x_left):
            self.step(self.player.y, x_left)
            self.player.left()

    def step_right(self):
        x_right = self.player.x+1
        if x_right > self.square.right_border:
            x_right = self.square.right_border

        if self.check_obstacle(self.player.y, x_right):
            self.step(self.player.y, x_right)
            self.player.right()

    def step_up(self):
        y_up = self.player.y+1
        if y_up > self.square.top_border:
            y_up = self.square.top_border

        if self.check_obstacle(y_up, self.player.x):
            self.step(y_up, self.player.x)
            self.player.up()

    def step_down(self):
        y_down = self.player.y-1
        if y_down < self.square.bottom_border:
            y_down = self.square.bottom_border
            
        if self.check_obstacle(y_down, self.player.x):
            self.step(y_down, self.player.x)
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


def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    if response == "y":
      return True
    elif response == "n":
      return False 


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


def check_loss(square, player):
    if square.count_energy() == 0 and \
        player.level_energy() == 0 and \
        square.count_obstacle() > 0:
        print('Losing!')
        return True

def check_win(square, player):
    if square.count_obstacle() == 0 and \
          square.count_energy() >= 0:
        print('Win!')
        return True

def check_game(square, player):
    return check_loss(square, player) or check_win(square, player)


def main():
    print("\t\tWelcome!\n")

    x_size = size_x()
    y_size = size_y()

    square = Field(x_size, y_size)
    player = Player(randint(x_size[0], x_size[1]), randint(y_size[0], y_size[1]))

    game = Moving(square, player)
    game.player_coordinate()


    action = None
    while not check_game(square, player):
        print()
        print(f'Energy: {player.energy}\n')
        game.render()
        action = ask_for_action("""
                Which way to take a step?:
                w - step up
                s - step down
                a - step left
                d - step right
                e - exit
                Enter: """)
        if action == 'e':
            break
        else:
            game.play(action)
        print()

print()
main()
