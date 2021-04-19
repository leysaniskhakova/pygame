
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

        self.__number_of_obstacles = len(self.__field)//3
        self.__x_obstacles = [choice(self.x_line) for y in range(self.__number_of_obstacles)]
        self.__y_obstacles = [choice(self.y_line) for y in range(self.__number_of_obstacles)]
        self.__obstacles = [(self.__y_obstacles[i], self.__x_obstacles[i]) for i in range(self.__number_of_obstacles)]

        for coordinate in self.__obstacles:
            if coordinate in self.__field.keys():
                self.__field[coordinate] = '#'


    def __getitem__(self, coordinate):
        return self.__field[coordinate]

    def __setitem__(self, coordinate, symbol):
        self.__field[coordinate] = symbol

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