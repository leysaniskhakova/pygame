from field import Field
from player import Player
from random import randint


class Moving(object):

    def __init__(self, square, player):
        self.square = square
        self.player = player

    def render(self): 
        self.square.render()

    def border_chek(self, y, x):
        if x < self.square.left_border:
            x = self.square.left_border
        elif x > self.square.right_border:
            x = self.square.right_border
        if y < self.square.bottom_border:
            y = self.square.bottom_border 
        elif y > self.square.top_border:
            y = self.square.top_border
        return y, x

    def player_symbol(self):
        self.square[self.player.get_coordinates()] = 'И'

    def check_energy(self, coordinate):
        if self.square.has_energy(coordinate):
            self.player.energy_increased()

    def check_obstacle(self, coordinate):
        if not self.square.has_obstacle(coordinate):
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
        next_coordinates = self.border_chek(y, x)
        if self.check_obstacle(next_coordinates):
            self.check_energy(next_coordinates)
            self.square.reset_old_position(self.player.get_coordinates())
            self.player.set_coordinates(next_coordinates)

    def play(self, action):

        if action == "a":
            self.step(self.player.y, self.player.x-1)
        elif action == "d":
            self.step(self.player.y, self.player.x+1)
        elif action == "w":
            self.step(self.player.y+1, self.player.x)
        elif action == "s":
            self.step(self.player.y-1, self.player.x)

        self.player_symbol()


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
    game.player_symbol()


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
