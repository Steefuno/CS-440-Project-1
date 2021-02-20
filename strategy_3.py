import bfs
import fire

# proceed from top-left to bottom right
def run(maze, flammability):
    start = (0, 0)
    end = (maze.height - 1, maze.width - 1)

    # setup the fire
    fire.add_fire(maze, flammability)

    # calculate the first path
    path = []
    bfs.bfs(path, maze, start, end)
    if len(path) == 0:  # No path found
        return None

    position_on_path = 0

    # tread the path
    while True:
        position_on_path += 1
        # step to next on path
        oop = False

        # if we stepped into fire, fail
        try:    # was giving an out of bounds error?
            if maze.maze[path[position_on_path][0]][path[position_on_path][1]] != 0:
                return False
        except IndexError:  # if theres an index error at the current pos something is definitely wrong
            return False

        # if we reached the end, pass
        if path[position_on_path] == end:
            return True

        # spread the fire
        fire.advance_fire_one_step(maze)

        # if fire moved onto us, fail
        if maze.maze[path[position_on_path][0]][path[position_on_path][1]] != 0:
            return False

        # recalculate path if an immediate neighbor is on fire
        try:    # catches an out of bounds error in case the agent is on the edge of the maze
            # west
            if not oop and maze.maze[path[position_on_path][0]][path[position_on_path][1]-1] == 2:
                bfs.bfs(path, maze, path[position_on_path], end)
                oop = True
        except IndexError:  # just used to satisfy the try-except
            oop = oop

        try:
            # east
            if not oop and maze.maze[path[position_on_path][0]][path[position_on_path][1]+1] == 2:
                bfs.bfs(path, maze, path[position_on_path], end)
                oop = True
        except IndexError:
            oop = oop

        try:
            # south
            if not oop and maze.maze[path[position_on_path][0]+1][path[position_on_path][1]] == 2:
                bfs.bfs(path, maze, path[position_on_path], end)
                oop = True
        except IndexError:
            oop = oop

        try:
            # north
            if not oop and maze.maze[path[position_on_path][0]-1][path[position_on_path][1]] == 2:
                bfs.bfs(path, maze, path[position_on_path], end)
                oop = True
        except IndexError:
            oop = oop

        if oop:
            position_on_path = 0
            if len(path) == 0:  # No path found
                return False

    return

# test
"""
import maze
m = maze.Maze(10, 10, .15)
print( run(m, .5) )
"""