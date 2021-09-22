from field import Field
from player import Player
import formatter
from random import randint


class Moving(object):

    def __init__(self, x_size, y_size):
 
        self.square = Field(x_size, y_size)

        self.x_start = randint(self.square.left_border+1, self.square.right_border-1)
        self.y_start = randint(self.square.bottom_border+1, self.square.top_border-1)

        self.player = Player(self.x_start, self.y_start)

        self.player_on_the_field = formatter.bg_purple(
                                    formatter.alignment(self.player.player_on_the_field, self.square.margin()))


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
