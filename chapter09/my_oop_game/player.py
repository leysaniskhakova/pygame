
class Player(object):

  player_on_the_field = '*'

    def __init__(self, x, y):
      self.x = x
      self.y = y
      self.energy = 0

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

    def set_coordinates(self, next_coordinates):
      self.y = next_coordinates[0]
      self.x = next_coordinates[1]

    def get_coordinates(self):
      return self.y, self.x

    def energy_increased(self):
      self.energy += 10

    def energy_decreased(self):
      self.energy -= 10

    def level_energy(self):
      return self.energy

    def __str__(self):
      return f'x:{self.x}, y:{self.y}, energy: {self.energy}'


if __name__ == "__main__":
    y = 1
    x = 1

    player = Player(x, y)
    print(player.get_coordinates())
    print(player)