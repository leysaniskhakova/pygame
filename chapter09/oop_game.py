#!/usr/bin/python3

from field import Field
from player import Player
import desing
from random import randint
import sys


class Moving(object):

    player_on_the_field = '*'

    def __init__(self, x_size, y_size):
 
        self.square = Field(x_size, y_size)

        self.x_start = randint(self.square.left_border+1, self.square.right_border-1)
        self.y_start = randint(self.square.bottom_border+1, self.square.top_border-1)

        self.player_on_the_field = desing.back_purple(
                                    desing.alignment(self.player_on_the_field, self.square.margin()))

        self.player = Player(self.x_start, self.y_start)

    def render(self): 
        self.square.render()

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
        self.square[self.player.y, self.player.x] = self.player_on_the_field

    def field_cell(self):
        self.square[self.player.y, self.player.x] = self.square.cell

    def step_left(self):
        self.field_cell()
        self.player.left()

    def step_right(self):
        self.field_cell()
        self.player.right()

    def step_up(self):
        self.field_cell()
        self.player.up()

    def step_down(self):
        self.field_cell()
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


def input_int(parameter, text=''):
    while True:
        print(f'{parameter}: ', end='')
        try:
            number = int(input(text))
            if number > 0:
                return number
            else:
                print(desing.out_red('\nThe number must be positive!'))
        except ValueError:
            print(desing.out_red('\nEnter the number!'))
            pass

def first_level():
    print(desing.out_green('\nEnter the size of the first playing field (number of cells in height and width):'))
    return input_int(desing.out_blue('\nwidth'))+1, input_int(desing.out_blue('\nheight'))+1

def next_level():
    print(desing.out_green('\nSelect how many cells the next field will be larger than the previous one'))
    return input_int(desing.out_blue('\nrise'))

def last_level():
    print(desing.out_green('\nEnter the number of levels'))
    return input_int(desing.out_blue('\nlevels'))


def ask_for_action(question):
    response = None
    while response not in ("w", "s", "a", "d", "e"):
        response = input(question).lower()
    return response

def input_data():
    level_fields = {}
    start = 0
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



def main():

    print(desing.out_yellow('\t\tWelcome!\n'))
    
    level_and_field = input_data()

    desing.clear()

    number_of_levels = 0

    for level in level_and_field:
        size_field = level_and_field[level]

        game = Moving(*size_field)

        action = None

        while game.exit_check() and action != 'e':
            print(desing.out_yellow(f'\t\tlevel: {level}\n'))
            game.render()
            action = ask_for_action(desing.out_red(step_question()))
            game.play(action)
            print()
        
            desing.clear()

        if action == 'e':
            print(desing.out_yellow('\n\t\tCome back!'))
            break
            
        number_of_levels += 1

    if number_of_levels == len(level_and_field):
        print(desing.out_yellow('\n\tCongratulations!\n\tYou have found a way out!'))

if __name__ == "__main__":
    print()
    main()
    input()
    sys.exit()
