import matplotlib.pyplot as plt
import numpy as np
import maze
import dfs

width = 100
height = 100
tries = 50
interval = .0625

densities = [] # X axis
probabilities = [] # Y axis

m = maze.Maze(width, height, .5)

density = 0
while density < 1: # for each density
    density += interval
    successes = 0

    i = 0
    while i < tries: # for each try, generate another maze and see if successful path
        i += 1
        m.generate_maze(density)
        if dfs.dfs([], m, (1, 1), (height - 2, width - 2)):
            successes += 1
    
    probability = successes / tries
    densities.append(density)
    probabilities.append(probability)

plt.plot(densities, probabilities)
plt.xlabel("Densities")
plt.ylabel("Probabilities")
plt.title("Probability of a Graph with a Path from Start to Finish with Varying Densities")
plt.show()