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

        self.x_line = [x for x in range(x_size[0], x_size[1]+1)]
        self.y_line = [y for y in range(y_size[0], y_size[1]+1)]

        self.__exit = random.choice(\
                    [(random.choice(y_size), random.randint(self.x_line[1], self.x_line[-2])),\
                    (random.randint(self.y_line[1], self.y_line[-2]), random.choice(x_size))])

        for y in self.y_line:
            for x in self.x_line:
                coordinate = y, x
                self.__field[coordinate] = self.out_green(self.cell)
                if coordinate != self.__exit:
                    if x == self.left_border or x == self.right_border:
                        self.__field[y+1, x] = self.__back_green(self.y_border)
                        self.__field[y, x] = self.__back_green(self.x_border)
                    if y == self.top_border or y == self.bottom_border:
                        self.__field[y, x] = self.__back_green(self.y_border)
                else:
                    self.__field[coordinate] = self.empty
                    
    
    def __getitem__(self, coordinate):
        return self.__field[coordinate]

    def __setitem__(self, coordinate, symbol):
        self.__field[coordinate] = symbol

    def exit_coordinate(self):
        return self.__exit

    def __back_green(self, text):
        return f'\033[32m\033[42m{text:{self.margin()}s}\033[0m'

    def out_green(self, text):
        return f'\033[2m\033[32m{text:{self.margin()}s}\033[0m'

    def out_yellow(self, text):
        return f'\033[33m{text:>{self.margin()}s}\033[0m'

    def out_turquoise(string):
        print(f'\033[1m\033[36m{string}\033[0m')

    def margin(self):    
        margin = max(
                len(str(self.x_line[0])),
                len(str(self.x_line[-1]))
            )+1
        return margin

    def render(self):

        for y in self.y_line:

            if y == self.y_line[0] or y == self.y_line[-1]:
                print(self.out_green(f'{"":10s}'), end='')
            else:
                print(self.out_green(f'{y:10d}'), end='')

            for x in self.x_line:
                coordinate = y, x
                print(f'{self.__field[coordinate]:>{self.margin()}s}', end='')

            print()

        x_line = f'{"":10s}'
        for x in self.x_line[1:-1]:
            x_line += f'{x:{self.margin()}d}'
        print(self.out_green(x_line))



if __name__ == "__main__":
    x_min, x_max = 1, 10
    y_min, y_max = 1, 10

    x_size = x_min-1, x_max+1
    y_size = y_min-1, y_max+1

    print(x_size, y_size)

    voc = Field(x_size, y_size)
    voc.render()
    print(voc.x_line, voc.x_line[1:-1])
    print(voc.y_line, voc.y_line[1:-1])
    print(voc.exit_coordinate())