
def left(coordinate):
    return coordinate[0], coordinate[1]-1

def right(coordinate):
    return coordinate[0], coordinate[1]+1

def up(coordinate):
    return coordinate[0]-1, coordinate[1]

def down(coordinate):
    return coordinate[0]+1, coordinate[1]

def route(response, coordinate):
    if response == 'a':
        coordinate = left(coordinate)
    elif response == 'd':
        coordinate = right(coordinate)
    elif response == 'w':
        coordinate = up(coordinate)
    elif response == 's':
        coordinate = down(coordinate)
    return coordinate
    