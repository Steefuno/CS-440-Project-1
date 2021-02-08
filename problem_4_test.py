import maze
import dfs
import bfs
import a
import time

max_dimensions = {
    "dfs" : None,
    "bfs" : None,
    "a*" : None,
}

search_functions = {
    "dfs" : dfs.dfs,
    "bfs" : bfs.bfs,
    "a*" : a.a
}

tries = 5
density = .3
size_increment = 100

def get_largest_dim(name):
    current_size = [0, 0]
    search_function = search_functions[name]

    average_time = 0
    # test different sized mazes until an average time above the limit is found
    while average_time < 60:
        current_size[0] += size_increment
        current_size[1] += size_increment
        m = maze.Maze(current_size[1], current_size[0], .5)

        i = 0

        total_time = 0
        while i < tries:
            i += 1
            m.generate_maze(density)

            start_time = time.time()
            search_function([], m, (1, 1), (current_size[0] - 2, current_size[1] - 2))
            end_time = time.time()
            total_time += end_time - start_time
        average_time = total_time / tries
        print(("\tAverage time for {name} in {width} by {height}: {average_time:.2f}").format(name = name, width = current_size[1], height = current_size[0], average_time = average_time))
    print()
    return current_size

for name in search_functions:
    max_dimensions[name] = get_largest_dim(name)

print("With density, .3, within a minute:")
for name in max_dimensions:
    print(("\t{name} can search a {width} by {height} maze").format(name = name, width = max_dimensions[name][1], height = max_dimensions[name][0]))