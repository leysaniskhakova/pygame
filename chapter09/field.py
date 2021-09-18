import random
import formatter


class Field(object):

    cell = '.'
    empty = ' '

    def __init__(self, x_size, y_size):
        self.__field = {}

        self.left_border = x_size[0]
        self.right_border = x_size[1]
        self.top_border = y_size[1]
        self.bottom_border = y_size[0]

        self.x_line = [x for x in range(x_size[0], x_size[1]+1)]
        self.y_line = [y for y in range(y_size[0], y_size[1]+1)]

        self.__exit = random.choice(\
                    [(random.choice(y_size), random.randint(self.x_line[1], self.x_line[-2])),\
                    (random.randint(self.y_line[1], self.y_line[-2]), random.choice(x_size))])

        self.cell = formatter.fg_green(formatter.alignment(self.cell, self.margin()))

        for y in self.y_line:
            for x in self.x_line:
                coordinate = y, x
                self.__field[coordinate] = self.cell
                if coordinate != self.__exit:
                    if x == self.left_border or x == self.right_border:
                        self.__field[coordinate] = formatter.bg_green(self.cell)
                    if y == self.top_border or y == self.bottom_border:
                        self.__field[coordinate] = formatter.bg_green(self.cell)
                else:
                    self.__field[coordinate] = self.empty
                    
    
    def __getitem__(self, coordinate):
        return self.__field[coordinate]

    def __setitem__(self, coordinate, symbol):
        self.__field[coordinate] = symbol

    def exit_coordinate(self):
        return self.__exit


    def margin(self):    
        margin = max(
                len(str(self.x_line[0])),
                len(str(self.x_line[-1]))
            )+1
        return margin

    def render(self):
        for y in self.y_line:
            print(formatter.fg_green(formatter.alignment("", 10)), end='')
            for x in self.x_line:
                coordinate = y, x
                # print(f'{self.__field[coordinate]:{self.margin()}s}', end='')
                print(formatter.alignment(self.__field[coordinate], self.margin()), end='')
            print()
        print(formatter.fg_green(formatter.alignment("", 10)))



if __name__ == "__main__":
    x_min, x_max = 1, 5
    y_min, y_max = 1, 5

    x_size = x_min-1, x_max+1
    y_size = y_min-1, y_max+1

    print(x_size, y_size)

    voc = Field(x_size, y_size)
    voc.render()
    print(voc.x_line, voc.x_line[1:-1])
    print(voc.y_line, voc.y_line[1:-1])
    print(voc.exit_coordinate())
    