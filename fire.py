import random

neighbors = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

# Sets the fire into the maze at position as 2
def add_fire(maze, flammability):
    # Note, if tile is a wall, we will replace the wall
    y = random.randrange(0, maze.height-1)
    x = random.randrange(0, maze.width-1)
    print("Inserted fire at {p}".format(p = (y, x)))
    maze.maze[y][x] = 2
    maze.flammability = flammability
    return

# Scans through maze to apply probability of spreading fire
def advance_fire_one_step(maze):
    new_fires = []
    # Check where should have fires
    for column in range(maze.height):
        for row in range(maze.width):
            if maze.maze[column][row] != 0:
                continue

            count = count_burning_neighbors(maze, (column, row))
            probability = 1 - pow(1 - maze.flammability, count)
            is_spread = (random.random() < probability)

            if is_spread == True:
                new_fires.append( (column, row) )
    # Apply fires
    for position in new_fires:
        maze.maze[position[0]][position[1]] = 2
    return

# Counts how many surrounding cells are lit aflame
def count_burning_neighbors(maze, position):
    count = 0
    for neighbor_offset in neighbors:
        neighbor = (
            position[0] + neighbor_offset[0],
            position[1] + neighbor_offset[1],
        )
        if (neighbor[0] < 0) or (neighbor[0] >= maze.height):
            continue
        if (neighbor[1] < 0) or (neighbor[1] >= maze.width):
            continue

        if maze.maze[neighbor[0]][neighbor[1]] == 2:
            count += 1
    return count

# example usage of fire.py
"""
import maze
m = maze.Maze(10, 10, .25)
m.output()

input()
add_fire(m, .5)
m.output()

while True:
    input()
    advance_fire_one_step(m)
    m.output()
"""