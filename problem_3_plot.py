import matplotlib.pyplot as plt
import maze
import a
import bfs

width = 100
height = 100
tries = 100
interval = .0625

densities = [] # X axis
avg_a_count = [] # Y axis 1
avg_bfs_count = [] # Y axis 2

m = maze.Maze(width, height, .5)

density = 0
while density < 1: # for each density
    density += interval
    a_count = 0
    bfs_count = 0

    i = 0
    while i < tries: # for each try, generate another maze and get the count
        i += 1
        m.generate_maze(density)
        a_result = a.a([], m, (1, 1), (height - 2, width - 2))
        bfs_result = bfs.bfs([], m, (1, 1), (height - 2, width - 2))

        if a_result != False:
            a_count += a_result
        if bfs_result != False:
            bfs_count += a_result
    
    densities.append(density)
    avg_a_count.append(a_count / tries)
    avg_bfs_count.append(bfs_count / tries)

plt.plot(densities, avg_a_count, label = "A*")
plt.plot(densities, avg_bfs_count, label = "BFS")
plt.xlabel("Densities")
plt.ylabel("Average Number of Nodes")
plt.title(("Number of Nodes Explored vs Density in Random {width} by {height} Maze").format(width = width, height = height))
plt.show()