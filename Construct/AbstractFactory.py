from Construct.Maze import Door, Wall, Maze, Room, walk_through_maze


class MazeFactory(object):

    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall()

    def make_room(self, n):
        return Room(n)

    def make_door(self, room1, room2):
        return Door(room1, room2)


class MagicDoor(Door):
    def enter(self):
        print 'Enter magic door'


class MagicWall(Wall):
    def enter(self):
        print 'Walk against a magic wall'


class MagicMaze(Maze):
    def enter(self):
        print 'Enter magic maze'


class MagicRoom(Room):
    def enter(self):
        print 'Enter magic room %s' % self.room_number


class MagicMazeFactory(MazeFactory):

    def make_wall(self):
        return MagicWall()

    def make_door(self, room1, room2):
        return MagicDoor(room1, room2)

    def make_maze(self):
        return MagicMaze()

    def make_room(self, n):
        return MagicRoom(n)


def createMaze(maze_factory):
    """
    we still got a tiny maze as before
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
    :param maze_factory: a abstract factory
    :return:
    """
    maze = maze_factory.make_maze()

    room1 = maze_factory.make_room(1)
    room2 = maze_factory.make_room(2)

    maze.add_section(room1)
    maze.add_section(room2)

    door = maze_factory.make_door(room1, room2)

    room1.set_side('North', door)
    room1.set_side('East', maze_factory.make_wall())
    room1.set_side('West', maze_factory.make_wall())
    room1.set_side('South', maze_factory.make_wall())

    room2.set_side('North', maze_factory.make_wall())
    room2.set_side('East', maze_factory.make_wall())
    room2.set_side('West', maze_factory.make_wall())
    room2.set_side('South', door)

    return maze


if __name__ == '__main__':
    maze_factory = MazeFactory()
    maze = createMaze(maze_factory)
    walk_through_maze(maze)

    magic_maze_factory = MagicMazeFactory()
    magic_maze = createMaze(magic_maze_factory)
    walk_through_maze(magic_maze)