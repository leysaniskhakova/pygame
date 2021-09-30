
import formatter


class Player(object):

    def __init__(self, coordinates, energy):
      self.y = coordinates[0]
      self.x = coordinates[1]
      self.energy = energy
      
    def get_player_coordinate(self):
      return self.y, self.x

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

    def energy_increased(self):
      self.energy += 10

    def energy_decreased(self):
      self.energy -= 10

    def energy_level(self):
      return self.energy

    def energy_no(self):
      return self.energy < 10

    def energy_is(self):
      return self.energy >= 10

    def energy_display(self):
      print(formatter.fg_blue(f'\t energy units: {self.energy}\n'))
