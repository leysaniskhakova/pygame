#!/usr/bin/python3

from field import Field
from player import Player
from moving import Moving
import formatter
import data
import sys


def main():

    print(formatter.fg_yellow('\t\tWelcome!\n'))
    
    level_and_field = data.input_data()

    formatter.clear()

    number_of_levels = 0

    for level in level_and_field:
        size_field = level_and_field[level]

        game = Moving(*size_field)

        action = None

        while game.exit_check() and action != 'e':
            print(formatter.fg_yellow(f'\t\tlevel: {level}\n'))
            game.render()
            action = data.ask_for_action(formatter.fg_red(data.step_question()))
            game.play(action)
            print()
        
            formatter.clear()

        if action == 'e':
            print(formatter.fg_yellow('\n\t\tCome back!'))
            break
            
        number_of_levels += 1

    if number_of_levels == len(level_and_field):
        print(formatter.fg_yellow('\n\tCongratulations!\n\tYou have found a way out!'))

if __name__ == "__main__":
    print()
    main()
    input()
    sys.exit()
