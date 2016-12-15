# -*- encoding=utf-8 -*-
"""
builder 模式
builder模式主要的特点在于可以控制"创建的过程"，
通过对创建过程和创建的基础模块的分离，使得对于
一个新的产品只需要实现一个新的创建过程；
"""
from Maze import Maze, Room, Door, Wall, walk_through_maze


class MazeBuilder(object):

    def __init__(self):
        self.maze = None

    def build_maze(self):
        if not self.maze:
            self.maze = Maze()
        return self.maze

    def build_room(self, number):
        room = Room(number)
        room.set_side('North', Wall())
        room.set_side('East', Wall())
        room.set_side('West', Wall())
        room.set_side('South', Wall())
        self.maze.add_section(room)
        return room

    def build_door(self, room1, room2):
        door = Door(room1, room2)

        room1.set_side('North', door)
        room2.set_side('South', door)
        return door

    def get_maze(self):
        return self.maze


def create_maze(builder):
    builder.build_maze()
    room1 = builder.build_room(1)
    room2 = builder.build_room(2)

    builder.build_door(room1, room2)

    return builder.get_maze()


def create_complex_maze(builder):
    builder.build_maze()
    rooms = []
    for i in range(100):
        rooms.append(builder.build_room(i))

    # do some more complex thing here

    return builder.get_maze()


if __name__ == '__main__':
    builder = MazeBuilder()
    maze = create_maze(builder)
    walk_through_maze(maze)

