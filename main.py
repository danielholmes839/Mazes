# Daniel Holmes
# main.py
# 2019/09/07

import turtle
import sys
from maze import Maze
from solver import Solver

sys.setrecursionlimit(100000)

MAZE_COLOR = '#000000'
SOLVER_COLOR = '#ff0000'
MAZE_SPEED = 10
SOLVER_SPEED = 2


maze = Maze(20, 20, MAZE_COLOR, MAZE_SPEED)
Solver(maze.nodes, SOLVER_COLOR, SOLVER_SPEED)

turtle.done()
