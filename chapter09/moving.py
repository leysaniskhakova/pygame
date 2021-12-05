from field import Field
from player import Player
import formatter
import data
import string
import way


class Moving(object):

    free_cell = 'free'

    def __init__(self, field, player):

        self.square = field
        self.player = player
        self.player_on_the_field = formatter.bg_purple(\
                                    formatter.alignment(self.square.cell, self.square.margin()))

    def render(self):
        self.handleCollisions()
        self.player_energy_display()
        self.square.render()

    def player_energy_display(self):
        data.print_blue_text(data.string_energy_units(self.player.energy_level()))

    def handleCollisions(self):

        player_coordinate = self.player.get_player_coordinate()

        if self.square.obstacle(player_coordinate):
            self.square.annihilation_obstacle(player_coordinate)

        if self.square.energy(player_coordinate):
            self.square.annihilation_energy(player_coordinate)

        self.square[player_coordinate] = self.player_on_the_field

    def check_exit(self):
        return self.player.get_player_coordinate() != self.square.exit_coordinate()

    def check_cell_energy(self):
        if self.square.energy(self.player.get_player_coordinate()):
            self.square.annihilation_energy(self.player.get_player_coordinate())
            self.player.energy_increased()

    def not_energy(self, response):
        if response and self.player.energy_no():
            data.message(string.lack_of_energy())

    def ask_about_annihilation(self):
        ask = formatter.fg_yellow(string.energy_question())
        return data.ask_yes_no(ask)

    def annihilation(self, coordinate):
        response = self.ask_about_annihilation()
        if response and self.player.energy_is():
            self.square.annihilation_obstacle(coordinate)
            self.player.energy_decreased()
            return self.free_cell
        return self.not_energy(response)
    
    def clean_cell(self):
        self.square[self.player.get_player_coordinate()] = self.square.cell

    def step_left(self):
        self.player.left()

    def step_right(self):
        self.player.right()

    def step_up(self):
        self.player.up()

    def step_down(self):
        self.player.down()

    def step(self, action):

        self.clean_cell()

        if action == 'a':
            self.step_left()
        elif action == 'd':
            self.step_right()
        elif action == 'w':
            self.step_up()
        elif action == 's':
            self.step_down()

        self.check_cell_energy()

    def status_coordinate(self, coordinate):
        if not self.square.border(coordinate) and not self.square.obstacle(coordinate):
            return self.free_cell
        elif self.square.exit(coordinate):
            return self.free_cell
        elif self.square.obstacle(coordinate):
            return self.annihilation(coordinate)

    def next_coordinate(self, action):
        coordinate = way.route(action, self.player.get_player_coordinate())
        return self.status_coordinate(coordinate)

    def play(self, action):
        if self.next_coordinate(action) == self.free_cell:
            self.step(action)
