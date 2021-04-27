
from random import choice 

class Field(object):

    def __init__(self, x_size, y_size):
        self.__field = {}

        self.left_border = x_size[0]
        self.right_border = x_size[1]
        self.top_border = y_size[1]
        self.bottom_border = y_size[0]

        self.x_line = range(x_size[0], x_size[1]+1)
        self.y_line = range(y_size[1], y_size[0]-1, -1)

        for y in self.y_line:
            for x in self.x_line:
                coordinate = y, x
                self.__field[coordinate] = '.'

        self.__obstacles = [(choice(self.y_line), choice(self.x_line))\
                            for i in range(len(self.__field)//3)]

        for coordinate in self.__obstacles:
            self.__field[coordinate] = '#'

        self.__energy = [(choice(self.y_line), choice(self.x_line))\
                         for i in range(len(self.__field)//4)]

        for coordinate in self.__energy:
            self.__field[coordinate] = '+'

    def __getitem__(self, coordinate):
        return self.__field[coordinate]

    def __setitem__(self, coordinate, symbol):
        self.__field[coordinate] = symbol

    def symbol_obstacle(self):
        return '#'

    def has_obstacle(self, y, x):
        return self.__field[y, x] == self.symbol_obstacle()

    def symbol_energy(self):
        return '+'

    def has_energy(self, y, x):
        return self.__field[y, x] == self.symbol_energy()

    def reset_old_position(self, y, x):
        self.__field[y, x] = '.'

    def count_symbol_obstacle(self):
        count = 0
        for value in self.__field.values():
            if value == self.symbol_obstacle():
                count += 1
        return count

    def count_symbol_energy(self):
        count = 0
        for value in self.__field.values():
            if value == self.symbol_energy():
                count += 1
        return count

    def render(self):
        margin = max(
            len(str(self.x_line.start)),
            len(str(self.x_line.stop-1))
        )+1

        for y in self.y_line:
            print(f'{y: 10d}', end='')
            for x in self.x_line:
                coordinate = y, x
                print(f'{self.__field[coordinate]:>{margin}s}', end='')
            print()

        x_line = f'{"":10s}'
        for x in self.x_line:
            x_line += f'{x:{margin}d}'
        print(x_line)


if __name__ == "__main__":
    y_size = 1, 10
    x_size = 1, 10

    voc = Field(y_size, x_size)
    voc.render()