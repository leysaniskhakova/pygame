#!/usr/bin/python3

from field import Field
from random import randint
import os
import sys

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
        self.y -= 1
        return self.y

    def down(self):
        self.y += 1
        return self.y

    def get_player_coordinate(self):
        return self.y, self.x

class Moving(object):

    def __init__(self, x_size, y_size):
 
        self.square = Field(x_size, y_size)

        self.x_start = randint(self.square.left_border+1, self.square.right_border-1)
        self.y_start = randint(self.square.bottom_border+1, self.square.top_border-1)

        self.square[self.y_start, self.x_start] = self.__out_yellow('*')

        self.player = Player(self.x_start, self.y_start)

    def render(self): 
        self.square.render()

    def start_coordinate(self):
        if self.square[self.player.y, self.player.x] == self.__out_yellow('*'):
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

    def __out_yellow(self, text):
        return f'\033[33m{text:>{self.square.margin()}s}\033[0m'

    def player_symbol(self):
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = self.__out_yellow('И')

    def step_left(self):
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = self.square.out_green('<')
        self.player.left()

    def step_right(self):
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = self.square.out_green('>')
        self.player.right()

    def step_up(self):
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = self.square.out_green('^')
        self.player.up()

    def step_down(self):
        if not self.start_coordinate():
            self.square[self.player.y, self.player.x] = self.square.out_green('v')
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

def print_string(string, margin):
    print(f'\033[33m{string:>{margin}s}\033[0m')

def out_turquoise(string):
    print(f'\033[1m\033[36m{string}\033[0m')


def main():

    action = None

    x, y = 1, 5
    while y <= 11:
        
        game = Moving(*[(x, y), (x, y)])

        while game.exit_check() and action != 'e':

            out_turquoise('\t\tWelcome!\n')

            if y == 5:
                print_string('First level!\n', 22)
            elif y == 8:
                print_string('Second level!\n', 26)
            elif y == 11:
                print_string('Third level!\n', 34)

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
        
            os.system('cls' if os.name == 'nt' else 'clear')

        if action == 'e':
            out_turquoise('\n\t\tCome back!')
            break
        elif y == 11:
            out_turquoise('\n\tCongratulations! You have found a way out!')

        y += 3

# print()
# main()

if __name__ == "__main__":
    print()
    main()
    input()
    sys.exit()