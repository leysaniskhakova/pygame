
class Player(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 10

    def left(self):
        self.x -= 1
        return self.x

    def right(self):
        self.x += 1
        return self.x

    def up(self):
        self.y += 1
        return self.y

    def down(self):
        self.y -= 1
        return self.y

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
    print(player)