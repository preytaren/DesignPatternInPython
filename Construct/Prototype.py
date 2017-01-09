# -*- encoding=utf-8 -*-
"""
Prototype 模式
"""
import copy

from Maze import Maze, Room, Wall, Door, walk_through_maze


class MazePrototypeFactory(object):

    def __init__(self, maze, door, wall, room):
        self._prototype_maze = maze
        self._prototype_door = door
        self._prototype_wall = wall
        self._prototype_room = room

    def make_maze(self):
        return self._prototype_maze.clone()

    def make_door(self, r1, r2):
        door = self._prototype_door.clone()
        door.set_room(r1, r2)
        return door

    def make_room(self, n):
        room = self._prototype_room.clone()
        room.set_number(n)
        return room

    def make_wall(self):
        return self._prototype_wall.clone()


class CloneMixin(object):

    def clone(self):
        return copy.deepcopy(self)


class MazePrototype(Maze, CloneMixin):
    pass


class RoomPrototype(Room, CloneMixin):

    def set_number(self, n):
        self.room_number = n


class DoorPrototype(Door, CloneMixin):

    def set_room(self, r1, r2):
        self.room1 = r1
        self.room2 = r2


class WallPrototype(Wall, CloneMixin):
    pass


def prototype_use_case():
    maze_prototype = MazePrototype()
    room_prototype = RoomPrototype(None)
    door_prototype = DoorPrototype(None, None)
    wall_prototype = WallPrototype()
    factory = MazePrototypeFactory(maze=maze_prototype,
                                   room=room_prototype,
                                   door=door_prototype,
                                   wall=wall_prototype)

    maze = factory.make_maze()

    r1 = factory.make_room(1)
    r2 = factory.make_room(2)

    maze.add_section(r1)
    maze.add_section(r2)

    door = factory.make_door(r1, r2)

    wall = factory.make_wall()

    r1.set_side('North', door)
    r1.set_side('East', wall)
    r1.set_side('West', wall)
    r1.set_side('South', wall)

    r2.set_side('North', wall)
    r2.set_side('East', wall)
    r2.set_side('West', wall)
    r2.set_side('South', door)

    walk_through_maze(maze)


if __name__ == '__main__':
    prototype_use_case()


