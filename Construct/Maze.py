class Maze(object):
    def __init__(self):
        self.rooms = {}

    def add_section(self, section):
        self.rooms[section.room_number]  = section

    def get_room(self, room_number):
        return self.rooms[room_number]


class Section(object):

    def enter(self):
        print 'Entering a Section'


class Door(Section):

    def __init__(self, room1, room2, is_open=True):
        self.room1 = room1
        self.room2 = room2
        self.is_open = is_open

    def enter(self):
        if self.is_open:
            print 'Enter a door'
        else:
            print 'Cannot enter a closed door'


class Wall(Section):
    def enter(self):
        print 'Walk against a wall'


class Room(Section):

    SIDES = ['North', 'East', 'West', 'South']

    def __init__(self, num):
        self.room_number = num
        self.sides = {}

    def set_side(self, side, section):
        if side in self.SIDES:
            self.sides[side] = section

    def get_side(self, side):
        if side in self.SIDES:
            return self.sides[side]

    def enter(self):
        print 'Enter room %s' % self.room_number


def createMaze():
    """
    hard code a maze here
    we've got a tiny maze like this one:
                N
            _________
           |         |
           |  room2  |
           |         |
        E  |== door==|  W
           |         |
           |  room1  |
           |_________|

                S
    :return:
    """
    maze = Maze()

    room1 = Room(1)
    room2 = Room(2)

    maze.add_section(room1)
    maze.add_section(room2)

    door = Door(room1, room2)

    room1.set_side('North', door)
    room1.set_side('East', Wall())
    room1.set_side('West', Wall())
    room1.set_side('South', Wall())

    room2.set_side('North', Wall())
    room2.set_side('East', Wall())
    room2.set_side('West', Wall())
    room2.set_side('South', door)

    return maze


def walk_through_maze(maze):
    room1 = maze.get_room(1)
    room1.enter()
    section = room1.get_side('North')
    section.enter()

if __name__ == '__main__':
    maze = createMaze()
    walk_through_maze(maze)
