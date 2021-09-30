from field import Field
from player import Player
import formatter
import data


class Moving(object):

    free_cell = 'free'

    def __init__(self, field, player):

        self.square = field
        self.player = player
        self.player_on_the_field = formatter.bg_purple(\
                                    formatter.alignment(self.square.cell, self.square.margin()))

    def render(self):
        self.coordinate_relation()
        self.player.energy_display()
        self.square.render()

    def coordinate_relation(self):
        if self.square.obstacle(self.player.get_player_coordinate()):
            self.square.annihilation_obstacle(self.player.get_player_coordinate())

        if self.square.energy(self.player.get_player_coordinate()):
            self.square.annihilation_energy(self.player.get_player_coordinate())

        self.square[self.player.get_player_coordinate()] = self.player_on_the_field

    def check_exit(self):
        return self.player.get_player_coordinate() != self.square.exit_coordinate()

    def check_cell_energy(self):
        if self.square.energy(self.player.get_player_coordinate()):
            self.square.annihilation_energy(self.player.get_player_coordinate())
            self.player.energy_increased()

    def not_energy(self, response):
        if response and self.player.energy_no():
            data.message('Lack of energy!')

    def ask_about_annihilation(self):
        ask = formatter.fg_yellow('Destroy an obstacle for 10 energy units? (y/n)\n')
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

        if action == "a":
            self.step_left()
        elif action == "d":
            self.step_right()
        elif action == "w":
            self.step_up()
        elif action == "s":
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
        
        if action == "a":
            coordinate = self.square.left(self.player.get_player_coordinate())
        elif action == "d":
            coordinate = self.square.right(self.player.get_player_coordinate())
        elif action == "w":
            coordinate = self.square.up(self.player.get_player_coordinate())
        elif action == "s":
            coordinate = self.square.down(self.player.get_player_coordinate())

        return self.status_coordinate(coordinate)

    def play(self, action):

        if self.next_coordinate(action) == self.free_cell:
            self.step(action)
