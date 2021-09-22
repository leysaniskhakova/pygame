import random
import formatter


# self.cell = formatter.fg_green(formatter.alignment(self.cell, self.margin()))

# self.field = {(y, x): self.cell for x in self.x_line for y in self.y_line}

class Field(object):

    cell = '.'
    empty = ' '
    symbol_obstacle = '#'
    symbol_energy = '+'

    def __init__(self, x_size, y_size):

        self.field = {}

        self.borders = [(y_size[0]-1, x) for x in range(x_size[0]-1, x_size[1]+2)] + \
                       [(y_size[1]+1, x) for x in range(x_size[0]-1, x_size[1]+2)] + \
                       [(y, x_size[0]-1) for y in range(y_size[0]-1, y_size[1]+2)] + \
                       [(y, x_size[1]+1) for y in range(y_size[0]-1, y_size[1]+2)]

        self.corners = [(y_size[0]-1, x_size[0]-1), (y_size[0]-1, x_size[1]+1), \
                        (y_size[1]+1, x_size[0]-1), (y_size[1]+1, x_size[1]+1)]
                        
        self.exit = random.choice(list(set(self.borders) - set(self.corners)))

        self.x_line = [x for x in range(x_size[0], x_size[1]+1)]
        self.y_line = [y for y in range(y_size[0], y_size[1]+1)]

        self.field_coordinates = [(y, x) for x in self.x_line for y in self.y_line]

        self.obstacles = [(random.choice(self.y_line), random.choice(self.x_line))\
                           for i in range(len(self.x_line)*len(self.y_line)//3)]

        self.energy = [(random.choice(self.y_line), random.choice(self.x_line))\
                        for i in range(len(self.x_line)*len(self.y_line)//4)]

        self.cell = formatter.alignment(self.cell, self.margin())

        for coordinate in self.borders:
            self.field[coordinate] = formatter.bg_green(self.cell)
            if coordinate == self.exit:
                self.field[coordinate] = self.empty

        for coordinate in self.field_coordinates:
            self.field[coordinate] = self.cell
            if coordinate in self.obstacles:
                self.field[coordinate] = formatter.bg_red(self.cell)
            if coordinate in self.energy:
                self.field[coordinate] = self.symbol_energy

    def __getitem__(self, coordinate):
        return self.__field[coordinate]

    def __setitem__(self, coordinate, symbol):
        self.__field[coordinate] = symbol

    def exit_coordinate(self):
        return self.__exit

    def has_obstacle(self, coordinate):
        return self.__field[coordinate] == self.symbol_obstacle

    def has_energy(self, coordinate):
        return self.__field[coordinate] == self.symbol_energy

    def reset_old_position(self, coordinate):
        self.__field[coordinate] = self.empty

    def __count_symbol(self, symbol):
        count = 0
        for value in self.__field.values():
            if value == symbol:
                count += 1
        return count

    def count_energy(self):
        return self.__count_symbol(self.symbol_energy)

    def count_obstacle(self):
        return self.__count_symbol(self.symbol_obstacle)

    def margin(self):    
        margin = max(
                len(str(self.x_line[0])),
                len(str(self.x_line[-1]))
            )+1
        return margin

    def render(self):

        y_line = [y_size[0]-1] + self.y_line + [y_size[1]+1]
        x_line = [x_size[0]-1] + self.x_line + [x_size[1]+1]

        for y in y_line:
            print(formatter.fg_green(formatter.alignment("", 10)), end='')
            for x in x_line:
                coordinate = y, x
                print(formatter.alignment(self.field[coordinate], self.margin()), end='')
            print()
        print(formatter.fg_green(formatter.alignment("", 10)))


            

if __name__ == "__main__":
    x_min, x_max = 0, 6
    y_min, y_max = 3, 11

    x_size = x_min, x_max
    y_size = y_min, y_max

    print(x_size, y_size)

    voc = Field(x_size, y_size)
    voc.render()
    print()
 