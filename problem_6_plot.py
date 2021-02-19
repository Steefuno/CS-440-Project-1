import strategy_1
import strategy_2
import strategy_3
import maze
import matplotlib.pyplot as plt
import json

width = 100
height = 100
density = 0.3
tries = 10
interval = .25

search_functions = {
    "strategy 1" : strategy_1.run,
    "strategy 2" : strategy_2.run,
    "strategy 3" : strategy_3.run,
}

success_rates = {}
for (strategy, _) in search_functions.items():
    success_rates[strategy] = []

flammabilities = []

m = maze.Maze(width, height, .5)

flammability = 0
while flammability <= 1:
    successes = {} # the number of successful paths for this flammability
    counts = {} # the number of attempts at paths for this flammability

    # initialize the two dictionaries
    for (strategy, _) in search_functions.items():
        successes[strategy] = 0
        counts[strategy] = 0

    for i in range(0, tries):
        m.generate_maze(density)
        for (strategy, search_function) in search_functions.items():
            result = search_function(m, flammability)
            if result == True: # if made a path
                successes[strategy] += 1
            if result != None: # if attempted a path on a maze with atleast one path
                counts[strategy] += 1

    flammabilities.append(flammability)
    print("\nFlammability: {0}".format(flammability))
    for (strategy, _) in search_functions.items():
        success_rate = 0
        if counts[strategy] > 0:
            success_rate = successes[strategy] / counts[strategy]
        print("{0} Success Rate: {1}".format(strategy, success_rate))
        success_rates[strategy].append(success_rate)
    flammability += interval

data = json.dumps({"success_rates": success_rates, "flammabilities": flammabilities}) # note, tuples will convert to lists
file = open("./test_results/Strategy 1 2 3 Success Rates vs. Flammability", "w+")
file.write(data)
file.close()

for (strategy, success_rate) in success_rates.items():
    plt.plot(flammabilities, success_rate, label = strategy)
plt.xlabel("Flammabilities")
plt.ylabel("Success Rates")
plt.legend()
plt.title("Success Rate vs Flammability")
plt.show()