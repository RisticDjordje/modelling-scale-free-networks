import networkx as nx
import matplotlib.pyplot as plt
import random

node_final = int(input("Number of nodes: "))

G = nx.Graph()
G.add_edge(1, 2)

edges = {1: 1, 2: 1}


def probability(num_of_edges, total_num_of_edges):
    probability = num_of_edges / (total_num_of_edges*2)
    return probability


for m in range(3, node_final+1):

    total_num_of_edges = G.number_of_edges()

    for i in edges.keys():
        if m == 0:
            pass
        else:
            edges[i] = G.degree(i)

    probabilities = []
    for i in edges.values():
        a = probability(i, total_num_of_edges)
        probabilities.append(a)

    degree = [probabilities[0]]
    sum = probabilities[0]

    for i in range(1, len(probabilities)):
        sum += probabilities[i]
        degree.append(sum)

    randomnumber = random.random()

    for i in range(len(degree)):
        if randomnumber < degree[i]:
            node = i+1
            break

    G.add_edge(m, node)
    edges[m] = G.degree(m)


# HISTOGRAM
degrees = dict(G.degree())
degree_values = sorted(set(degrees.values()))
histogram = [list(degrees.values()).count(i)/float(nx.number_of_nodes(G)) for i in degree_values]

plt.figure()
plt.bar(degree_values, histogram)
plt.title('Degree Distribution of Graph')
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')

plt.axes([0.4, 0.4, 0.5, 0.48])

pos = nx.spring_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=10)
nx.draw_networkx_edges(G, pos, alpha=0.4)

plt.show()
