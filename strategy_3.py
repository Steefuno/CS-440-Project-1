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
        # step to next on path
        position_on_path += 1
        oop = False

        # if we stepped into fire, fail
        try:    # was giving an out of bounds error?
            if maze.maze[path[position_on_path][0]][path[position_on_path][1]] != 0:
                return False
        except IndexError:  # if theres an index error at the current pos something is definitely wrong
            return False

        # if we reached the end, pass
        if position_on_path == len(path) - 1:
            return True

        # spread the fire
        fire.advance_fire_one_step(maze)

        # if fire moved onto us, fail
        if maze.maze[path[position_on_path][0]][path[position_on_path][1]] != 0:
            return False

        # recalculate path if an immediate neighbor is on fire
        try:    # catches an out of bounds error in case the agent is on the edge of the maze
            # west
            if maze.maze[path[position_on_path+1][0]][path[position_on_path][1]] != 0:
                bfs.bfs(path, maze, path[1], end)
                oop = True
        except IndexError:  # just used to satisfy the try-except
            oop = oop

        try:
            # east
            if maze.maze[path[position_on_path-1][0]][path[position_on_path][1]] != 0:
                bfs.bfs(path, maze, path[1], end)
                oop = True
        except IndexError:
            oop = oop

        try:
            # south
            if maze.maze[path[position_on_path][0]][path[position_on_path+1][1]] != 0:
                bfs.bfs(path, maze, path[1], end)
                oop = True
        except IndexError:
            oop = oop

        try:
            # north
            if maze.maze[path[position_on_path][0]][path[position_on_path-1][1]] != 0:
                bfs.bfs(path, maze, path[1], end)
                oop = True
        except IndexError:
            oop = oop

        if oop:
            if len(path) == 0:  # No path found
                return False

    return
