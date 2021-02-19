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

        # if we stepped into fire, fail
        if maze.maze[path[position_on_path][0]][path[position_on_path][1]] != 0:
            return False

        # if we reached the end, pass
        if position_on_path == len(path) - 1:
            return True

        # spread the fire
        fire.advance_fire_one_step(maze)
        maze.output()

        # if fire moved onto us, fail
        if maze.maze[path[position_on_path][0]][path[position_on_path][1]] != 0:
            return False

        # recalculate path if an immediate neighbor is on fire
        oop = False
        if maze.maze[path[position_on_path+1][0]][path[position_on_path][1]] != 0:
            bfs.bfs(path, maze, path[1], end)
            oop = True
        elif maze.maze[path[position_on_path-1][0]][path[position_on_path][1]] != 0:
            bfs.bfs(path, maze, path[1], end)
            oop = True
        elif maze.maze[path[position_on_path][0]][path[position_on_path+1][1]] != 0:
            bfs.bfs(path, maze, path[1], end)
            oop = True
        elif maze.maze[path[position_on_path][0]][path[position_on_path-1][1]] != 0:
            bfs.bfs(path, maze, path[1], end)
            oop = True
        if oop:
            if len(path) == 0:  # No path found
                print("\nNo possible paths")
                return False
    return