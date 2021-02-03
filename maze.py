import numpy as np
import random as r

class Maze:
    # Creates a Maze instance
    def __init__(self, width, height, density):
        assert (width > 0), "width needs to be > 0"
        assert (height > 0), "height needs to be > 0"
        assert (density > 0) and (density < 1), "density needs to be (0, 1)"

        self.width = width # Number of columns
        self.height = height # Number of rows
        self.density = density # Probability of a given cell to be filled
        self.maze = self.generate_maze(width, height, density) # [y][x], 0 := open, 1 := barrier
        return

    # Generates the randomly set maze
    def generate_maze(self, width, height, density):
        maze = np.empty((height, width), np.bool8)

        # Set barriers based on density
        for index, _ in np.ndenumerate(maze):
            maze[index[0]][index[1]] = (r.random() < density)

        self.maze = maze
        return maze

    # Displays the maze as 1s and 0s
    def output(self):
        for row in self.maze:
            temp_arr = np.empty(self.width)
            for col_n, cell in enumerate(row):
                temp_arr[col_n] = 1 if (cell == True) else 0
            print(temp_arr)
        return