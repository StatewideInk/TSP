from networkx.readwrite.graph6 import write_graph6_file
from networkx.algorithms.boundary import node_boundary
from networkx.algorithms import approximation as approx

import networkx as nx
import matplotlib.pyplot as plt
import random
import array as arr

# Constants
numCities = 7
numChromo = 5
G = nx.complete_graph(numCities)
cycleArr = []
parent1 = []
parent2 = []
child = []

temp = 0
parentPos = 0
childPos = 0

for(u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(0, 1000)
    print(u, v, G.edges[u,v])

for i in range(numChromo):
    temp1 = random.randint(0, numCities - 2)
    temp2 = random.randint(0, numCities - 2)
    cycle = approx.simulated_annealing_tsp(G, "greedy", source = 0, alpha = 0.01)

    cycle.pop(0)
    cycle.pop(numCities - 1)

    cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
    cycle[temp1], cycle[temp2] = cycle[temp2], cycle[temp1]
    cycleArr.append(cycle)

# Creating crossover points
crossPoint1 = random.randint(1, numCities - 2)
crossPoint2 = random.randint(1, numCities - 2)
while(crossPoint1 == crossPoint2):
    crossPoint2 = random.randint(1, numCities - 2)
if(crossPoint1 > crossPoint2):
    temp = crossPoint1
    crossPoint1 = crossPoint2
    crossPoint2 = temp

print("crossTemp1:", crossPoint1)
print("crossTemp2:", crossPoint2)

temp = crossPoint1
for i in range(1):
    parent1 = cycleArr[random.randint(0, numChromo - 1)]
    parent2 = cycleArr[random.randint(0, numChromo - 1)]
    while(parent1 == parent2):
        parent2 = cycleArr[random.randint(0, numChromo - 1)]

    print("parent1:", parent1)
    print("parent2:", parent2)

    j = crossPoint1
    while j <= crossPoint2:
        print("parent1[j]:", parent1[j])
        child.append(parent1[j])
        j += 1
    print("Initial Segment:", child)

    parentPos = crossPoint2
    childPos = crossPoint2
    while(childPos != crossPoint1):
        if(parent2[parentPos] in child):
            if(parentPos >= numCities - 2):
                parentPos = 0
                print("parentPos:", parentPos)
            else:
                parentPos +=1
                print("parentPos:", parentPos)
        else:
            child.insert(childPos, parent2[parentPos])
            if(parentPos < numCities - 2):
                parentPos += 1
                childPos += 1
                if(childPos >= numCities - 2):
                    childPos = 0
                    print("childPos:", childPos)
                if(parentPos >= numCities - 2):
                    parentPos = 0
                    print("parentPos:", parentPos)
                print("parentPos:", parentPos)
                print("childPos:", childPos)

    print("Child:", child)