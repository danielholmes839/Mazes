# Daniel Holmes
# node.py
# 2019/09/07

import turtle
import random

DISTANCE = 10


class Node:
    def __init__(self, x, y, i):
        """ Create a node in the maze """
        self.x = x
        self.y = y
        self.index = i
        self.neighbours = []
        self.connections = []
        self.connected = False
        self.previous = 0

    def connect(self):
        """ Connect the node to a neighbour """
        options = self.get_connection_options()

        if options:
            # Connect to an option
            choice = random.choice(options)
            choice.connected = True
            choice.connections.append(self)

            self.connections.append(choice)
            self.lineto(choice)
            choice.connect()

        else:
            # Backtrack
            self.backtrack()

    def get_connection_options(self):
        """ Get neighbours which have no connections """
        return [neighbour for neighbour in self.neighbours if not neighbour.connected]

    def backtrack(self):
        """ Back tracks nodes until it arrives on a node where connections can be made """
        if self.get_connection_options():
            r = random.random()
            g = random.random()
            b = random.random()
            turtle.color((r, g, b))
            self.connect()

        elif self.index:
            self.connections[0].backtrack()

        else:
            print('Completed Maze')

    def lineto(self, node):
        """ Draw a line from this node to another node """
        turtle.up()
        turtle.goto(self.x * DISTANCE, self.y * DISTANCE)
        turtle.down()
        turtle.goto(node.x * DISTANCE, node.y * DISTANCE)
