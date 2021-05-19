import random


class Field(object):

    cell = '.'
    empty = ' '
    y_border = '_'
    x_border = '|'

    def __init__(self, x_size, y_size):
        self.__field = {}

        self.left_border = x_size[0]
        self.right_border = x_size[1]
        self.top_border = y_size[1]
        self.bottom_border = y_size[0]

        self.x_line = range(x_size[0], x_size[1]+1)
        self.y_line = range(y_size[1], y_size[0]-1, -1)

        self.__exit = random.choice(\
                    [(random.choice(y_size), random.randint(self.left_border+1, self.right_border-1)),\
                     (random.randint(self.bottom_border+1, self.top_border-1), random.choice(y_size))])

        for y in self.y_line:
            for x in self.x_line:
                coordinate = y, x
                self.__field[coordinate] = self.cell
                if coordinate != self.__exit:
                    if x == self.left_border or x == self.right_border:
                        self.__field[y-1, x] = self.y_border
                        self.__field[y, x] = self.x_border
                    if y == self.top_border or y == self.bottom_border:
                        self.__field[y, x] = self.y_border
                else:
                    self.__field[coordinate] = self.empty

        if self.__exit[1] == self.left_border or self.__exit[1] == self.right_border:
            self.__field[self.__exit[0]-1, self.__exit[1]] = self.y_border
            self.__field[self.__exit[0]+1, self.__exit[1]] = self.y_border
        elif self.__exit[0] == self.top_border or self.__exit[0] == self.bottom_border:
            self.__field[self.__exit[0], self.__exit[1]-1] = self.x_border
            self.__field[self.__exit[0], self.__exit[1]+1] = self.x_border

    
    def __getitem__(self, coordinate):
        return self.__field[coordinate]

    def __setitem__(self, coordinate, symbol):
        self.__field[coordinate] = symbol

    def exit_coordinate(self):
        return self.__exit

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
    print(voc.exit_coordinate())