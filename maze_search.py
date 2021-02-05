import numpy as np
import maze as m

# the neighbors checked when scanning neighbors
neighbors = [
    (-1, 0), # one space above
    (0, 1),
    (1, 0),
    (0, -1),
]

# the search starts at [start[0]][start[1]] and searches for [end[0][end[1]]
# only works for rectangular mazes
# assumes the params are valid
def dfs(path, maze, start, end):
    stack = [ start ]
    predecessors = {
        start : start,
    }
    distances = {
        start : 0
    }

    while len(stack) > 0:
        current = stack.pop(0) # pop from fringe
        dfs_insert_neighbors(maze, current, stack, predecessors, distances) # add current's neighbors to stack and update distances
    
    if end in predecessors: # compile the path if end is found
        compile_path(path, end, predecessors)
        return
    else:
        return

# updates the predecessors if possible for the current cell's neighbors and inserts back into the stack
def dfs_insert_neighbors(maze, current, stack, predecessors, distances):
    for neighbor_offset in neighbors:
        neighbor = (
            current[0] + neighbor_offset[0],
            current[1] + neighbor_offset[1],
        )

        # if neighbor doesn't exist (out of bounds), skip
        if (neighbor[0] < 0) or (neighbor[1] < 0):
            continue
        if (neighbor[0] >= maze.height) or (neighbor[1] >= maze.width):
            continue
        # if neighbor is not an open space
        if maze.maze[neighbor[0]][neighbor[1]] != 0:
            continue

        # if path from current to neighbor is closer than neighbor's current path
        if (neighbor not in distances) or (distances[neighbor] > distances[current] + 1):
            predecessors[neighbor] = current
            distances[neighbor] = distances[current] + 1
            stack.insert(0, neighbor)
        

# assembles the path given the end, predecessors, and distances
# [start, ... , end]
def compile_path(path, end, predecessors):
    current = end
    path.insert(0, current)
    while predecessors[current] != current: # while current isn't the start
        current = predecessors[current]
        path.insert(0, current)
    return

# example usage of maze_search.py
"""
maze = m.Maze(10, 10, .25)
maze.output()
path = []
dfs(
    path,
    maze,
    (1, 1),
    (8, 8)
)
print(path)
"""