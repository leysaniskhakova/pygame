
class Field(object):

    def __init__(self, x_size, y_size):
        self.field = {}

        self.x_line = range(x_size[0], x_size[1]+1)
        self.y_line = range(y_size[1], y_size[0]-1, -1)


        for y in self.y_line:
            for x in self.x_line:
                coordinate = y, x
                self.field[coordinate] = '.'

    def dict(self):
        return self.field

    def render(self):
        margin = max(
            len(str(self.x_line.start)),
            len(str(self.x_line.stop-1))
        )+1

        for y in self.y_line:
            print(f'{y: 10d}', end='')
            for x in self.x_line:
                coordinate = y, x
                print(f'{self.field[coordinate]:>{margin}s}', end='')
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