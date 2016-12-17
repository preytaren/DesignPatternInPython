# -*- encoding=utf-8 -*-
"""
Factory Method 模式

"""
from Maze import Room, Door, Wall, Maze, walk_through_maze
from AbstractFactory import MagicMaze, MagicDoor, MagicRoom, MagicWall


class MazeFactory(object):

    @classmethod
    def create_maze(cls):
        maze = cls.make_maze()

        r1 = cls.make_room(1)
        r2 = cls.make_room(2)

        maze.add_section(r1)
        maze.add_section(r2)

        door = cls.make_door(r1, r2)

        r1.set_side('North', door)
        r1.set_side('East', Wall())
        r1.set_side('West', Wall())
        r1.set_side('South', Wall())

        r2.set_side('North', Wall())
        r2.set_side('East', Wall())
        r2.set_side('West', Wall())
        r2.set_side('South', door)

        return maze

    @staticmethod
    def make_maze():
        return Maze()

    @staticmethod
    def make_room(n):
        return Room(n)

    @staticmethod
    def make_door(room1, room2):
        return Door(room1, room2)

    @staticmethod
    def make_wall():
        return Wall()


class MagicMazeFactory(MazeFactory):

    @staticmethod
    def make_maze():
        return MagicMaze()

    @staticmethod
    def make_room(n):
        return MagicRoom(n)

    @staticmethod
    def make_door(room1, room2):
        return MagicDoor(room1, room2)

    @staticmethod
    def make_wall():
        return MagicWall()


if __name__ == '__main__':
    maze = MazeFactory.create_maze()
    walk_through_maze(maze)

    magic_maze = MagicMazeFactory.create_maze()
    walk_through_maze(magic_maze)
