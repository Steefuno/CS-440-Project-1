import numpy
import random

class Maze:
    # Creates a Maze instance
    def __init__(self, width, height, density):
        assert(width > 0, "width needs to be > 0")
        assert(height > 0, "height needs to be > 0")
        assert((density > 0) and (density < 1), "density needs to be (0, 1)")

        self.width = width # Number of columns
        self.height = height # Number of rows
        self.density = density # Probability of a given cell to be filled
        self.maze = numpy.empty([height, width])
        self.generate_maze(density) # [y][x], 0 := open, 1 := barrier
        return

    # Generates the randomly set maze
    def generate_maze(self, density):
        # Set barriers based on density
        for index, _ in numpy.ndenumerate(self.maze):
            self.maze[index[0]][index[1]] = (random.random() < density)
        return

    # Displays the maze as 1s and 0s
    def output(self):
        for row in self.maze:
            temp_arr = numpy.empty(self.width)
            for col_n, cell in enumerate(row):
                temp_arr[col_n] = cell
            print(temp_arr)
        return

# example usage of maze.py
"""
maze = m.Maze(10, 10, .25)
maze.output()
"""