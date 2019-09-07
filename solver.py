# Daniel Holmes
# solver.py
# 2019/09/07

import turtle


class Solver:
    def __init__(self, nodes, color, speed):
        """ Solves the maze using a list of nodes """
        turtle.color(color)
        turtle.speed(speed)

        self.nodes = nodes
        self.start = nodes[0]
        self.end = nodes[-1]
        self.queue = [self.start]
        self.solution = []
        self.bfs()
        self.solve()

    def bfs(self):
        """ Breadth first search """
        for node in self.queue:

            if node.index == self.end.index:
                break

            for connection in node.connections:
                if node.previous != connection.index:

                    connection.previous = node.index
                    self.queue.append(connection)

    def solve(self):
        """ Solve the maze """
        prev = self.end
        self.solution = [prev]
        self.queue.reverse()

        for node in self.queue:
            if node.index in [connection.index for connection in prev.connections]:
                prev.lineto(node)
                prev = node
                self.solution.append(node)
