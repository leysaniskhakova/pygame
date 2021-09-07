
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
