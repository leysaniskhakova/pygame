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

    def player_energy(self, y, x):
      if self.square.has_energy(y, x):
        self.player.energy_increased()
        return False
      elif self.square.has_obstacle(y, x):
        return self.annihilation(y, x)

    def annihilation(self, y, x):
        question = ask_yes_no('Destroy an obstacle for 10 energy units? (y/n)\n')
        if question:
          if self.player.level_energy() > 0:
            self.player.energy_decreased()
            return False
          else:
            print('Lack of energy!')
            return True
        return True

    def check_step_left(self):
        x_left = self.player.x-1
        if x_left < self.square.left_border:
            x_left = self.square.left_border
        return self.player_energy(self.player.y, x_left)

    def check_step_right(self):
        x_right = self.player.x+1
        if x_right > self.square.right_border:
            x_right = self.square.right_border
        return self.player_energy(self.player.y, x_right)

    def check_step_up(self):
        y_up = self.player.y+1
        if y_up > self.square.top_border:
            y_up = self.square.top_border
        return self.player_energy(y_up, self.player.x)

    def check_step_down(self):
        y_down = self.player.y-1
        if y_down < self.square.bottom_border:
            y_down = self.square.bottom_border
        return self.player_energy(y_down, self.player.x)

    def step_left(self):
        if not self.check_step_left():
            self.square.reset_old_position(self.player.y, self.player.x)
            self.player.left()
    
    def step_right(self):
        if not self.check_step_right():
            self.square.reset_old_position(self.player.y, self.player.x)
            self.player.right()

    def step_up(self):
        if not self.check_step_up():
            self.square.reset_old_position(self.player.y, self.player.x)
            self.player.up()

    def step_down(self):
        if not self.check_step_down():
            self.square.reset_old_position(self.player.y, self.player.x)
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


def check_game(square, player):
    if square.count_symbol_energy() == 0 and \
        player.level_energy() == 0 and \
        square.count_symbol_obstacle() > 0:
        print('Losing!')
        return True
    elif square.count_symbol_obstacle() == 0 and \
          square.count_symbol_energy() >= 0:
        print('Win!')
        return True


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
                Enter: """)
        game.play(action)
        print()

print()
main()
