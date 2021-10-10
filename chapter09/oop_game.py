#!/usr/bin/python3

from field import Field
from player import Player
from moving import Moving
from random import choice
import formatter
import data
import sys


def main():

    data.print_yellow_text(data.welcome())
    
    level_and_field = data.input_data()

    formatter.clear()

    number_of_levels = 0
    player_energy = 0

    for level in level_and_field:
        size_field = level_and_field[level]

        field = Field(size_field[0], size_field[1])
        player = Player(choice(field.field_coordinates), player_energy)

        game = Moving(field, player)

        action = None

        while game.check_exit():
            data.print_yellow_text(data.variable_text(data.string_level(), level))
            game.render()
            action = data.ask_for_action(formatter.fg_red(data.step_question()))
            if action != data.stop():
                game.play(action)
            else:
                data.print_yellow_text(data.goodbye())
                break

            formatter.clear()

        if action == data.stop():
            break
            
        number_of_levels += 1
        player_energy = player.energy_level()

    if number_of_levels == len(level_and_field):
        data.print_yellow_text(data.congratulation())

if __name__ == "__main__":
    print()
    main()
    input()
    sys.exit()
