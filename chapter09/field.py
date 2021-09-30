from random import choice
import formatter


class Field(object):

    cell = '.'
    empty = ' '
    symbol_energy = '+'

    def __init__(self, width, height):

        self.__field = {}

        self.borders = [(height[0]-1, x) for x in range(width[0]-1, width[1]+2)] + \
                       [(height[1]+1, x) for x in range(width[0]-1, width[1]+2)] + \
                       [(y, width[0]-1) for y in range(height[0]-1, height[1]+2)] + \
                       [(y, width[1]+1) for y in range(height[0]-1, height[1]+2)]

        self.__corners = [(height[0]-1, width[0]-1), (height[0]-1, width[1]+1), \
                        (height[1]+1, width[0]-1), (height[1]+1, width[1]+1)]
                        
        self.__exit = choice(list(set(self.borders) - set(self.__corners)))

        self.__x_line = [x for x in range(width[0], width[1]+1)]
        self.__y_line = [y for y in range(height[0], height[1]+1)]
        self.all_height = [height[0]-1] + self.__y_line + [height[1]+1]
        self.all_width  = [width[0]-1] + self.__x_line + [width[1]+1]

        self.field_coordinates = [(y, x) for x in self.__x_line for y in self.__y_line]

        self.__obstacles = [(choice(self.__y_line), choice(self.__x_line))\
                           for i in range(len(self.field_coordinates)//3)]

        self.__energy = [(choice(self.__y_line), choice(self.__x_line))\
                        for i in range(len(self.field_coordinates)//4)]

        self.cell = formatter.alignment(self.cell, self.margin())
        self.symbol_energy = formatter.alignment(self.symbol_energy, self.margin())

        for coordinate in self.borders:
            self.__field[coordinate] = formatter.bg_green(self.cell)
            if coordinate == self.__exit:
                self.__field[coordinate] = self.empty

        for coordinate in self.field_coordinates:
            self.__field[coordinate] = self.cell
            if coordinate in self.__energy:
                self.__field[coordinate] = formatter.fg_yellow(self.symbol_energy)
            if coordinate in self.__obstacles:
                self.__field[coordinate] = formatter.bg_green(self.cell)


    def __getitem__(self, coordinate):
        return self.__field[coordinate]

    def __setitem__(self, coordinate, symbol):
        self.__field[coordinate] = symbol

    def empty_cell(self, coordinate):
        self.__field[coordinate] = self.empty

    def exit(self, coordinate):
        return coordinate == self.__exit

    def exit_coordinate(self):
        return self.__exit

    def obstacle(self, coordinate):
        return coordinate in self.__obstacles

    def border(self, coordinate):
        return coordinate in self.borders

    def energy(self, coordinate):
        return coordinate in self.__energy

    def annihilation_energy(self, coordinate):
        self.__energy.remove(coordinate)
        self.empty_cell(coordinate)

    def annihilation_obstacle(self, coordinate):
        self.__obstacles.remove(coordinate)
        self.empty_cell(coordinate)
        
    def left(self, coordinate):
        return coordinate[0], coordinate[1]-1

    def right(self, coordinate):
        return coordinate[0], coordinate[1]+1

    def up(self, coordinate):
        return coordinate[0]-1, coordinate[1]

    def down(self, coordinate):
        return coordinate[0]+1, coordinate[1]

    def margin(self):    
        margin = max(
                len(str(self.__x_line[0])),
                len(str(self.__x_line[-1]))
            )+1
        return margin

    def render(self):

        for y in self.all_height:
            print(formatter.fg_green(formatter.alignment("", 10)), end='')
            for x in self.all_width:
                coordinate = y, x
                print(formatter.alignment(self.__field[coordinate], self.margin()), end='')
            print()
        print(formatter.fg_green(formatter.alignment("", 10)))


            

if __name__ == "__main__":
    width, height = (0, 4), (0, 4)

    voc = Field(width, height)
    voc.render()
    print()
 