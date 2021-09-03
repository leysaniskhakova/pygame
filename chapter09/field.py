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

        if self.__exit[1] == self.left_border or self.__exit[1] == self.right_border:
            self.__field[self.__exit[0]-1, self.__exit[1]] = self.__back_green(self.y_border)
            self.__field[self.__exit[0]+1, self.__exit[1]] = self.__back_green(self.y_border)
        elif self.__exit[0] == self.top_border or self.__exit[0] == self.bottom_border:
            self.__field[self.__exit[0], self.__exit[1]-1] = self.__back_green(self.x_border)
            self.__field[self.__exit[0], self.__exit[1]+1] = self.__back_green(self.x_border)

    
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

    def margin(self):    
        margin = max(
                len(str(self.x_line[0])),
                len(str(self.x_line[-1]))
            )+1
        return margin

    def render(self):

        for y in self.y_line:
            print(self.out_green(f'{y: 10d}'), end='')
            for x in self.x_line:
                coordinate = y, x
                print(f'{self.__field[coordinate]:>{self.margin()}s}', end='')
            print()

        x_line = f'{"":10s}'
        for x in self.x_line:
            x_line += f'{x:{self.margin()}d}'
        print(self.out_green(x_line))



if __name__ == "__main__":
    x_size = -15, -5
    y_size = -10, 0

    voc = Field(x_size, y_size)
    voc.render()
    print(voc.x_line, voc.x_line[1:-1])
    print(voc.y_line, voc.y_line[1:-1])
    print(voc.exit_coordinate())