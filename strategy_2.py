import bfs
import fire

# proceed from top-left to bottom right
def run(maze, flammability):
    start = (0, 0)
    end = (maze.height-1, maze.width-1)

    # setup the fire
    fire.add_fire(maze, flammability)

    # calculate the first path
    path = []
    bfs.bfs(path, maze, start, end)
    if len(path) == 0: # No path found
        return None

    print("At: {0}, To: {1}".format(path[0], path[1]))

    # step on the path, spread fire, then create a new path
    while True:
        # if we stepped into fire, fail
        if maze.maze[ path[1][0] ][ path[1][1] ] != 0:
            print("Stepped info fire")
            return False

        # if we reached the end, pass
        if path[1] == end:
            print("Reached end")
            return True

        # spread the fire
        fire.advance_fire_one_step(maze)
        print("Fire advanced. New Maze:")
        maze.output()

        # if fire moved onto us, fail
        if maze.maze[ path[1][0] ][ path[1][1] ] != 0:
            print("Caught by fire")
            return False

        # recalculate path
        bfs.bfs(path, maze, path[1], end)
        if len(path) == 0: # No path found
            print("\nNo possible paths")
            return False
        print("\nAt: {0}, To: {1}".format(path[0], path[1]))
    return


# example usage of strategy_1.py

import maze
m = maze.Maze(10, 10, .15)
print( run(m, .5) )
