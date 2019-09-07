# Daniel Holmes
# maze.py
# 2019/09/07

import turtle
from node import Node


class Maze:
    def __init__(self, w, h, color, speed):
        """ Create a maze """
        turtle.color(color)
        turtle.speed(speed)

        self.w = w
        self.h = h
        self.nodes = []

        # Creates the maze
        self.create_nodes()
        self.create_neighbours()
        self.create()

    def create_nodes(self):
        """ Creates a grid of nodes """
        for x in range(self.w):
            for y in range(self.h):

                i = (y*self.w)+x                    # Index in array
                self.nodes.append(Node(x, y, i))    # Add to list of nodes

    def create_neighbours(self):
        """ Identify each nodes neighbours """
        for node in self.nodes:
            for neighbour in self.nodes:

                dx = abs(node.x - neighbour.x)
                dy = abs(node.y - neighbour.y)

                if dx + dy == 1:
                    node.neighbours.append(neighbour)

    def create(self):
        """ Creates the first connection the rest is recursive """
        start = self.nodes[0]
        start.connected = True
        start.connect()  # Recursively connect all nodes
