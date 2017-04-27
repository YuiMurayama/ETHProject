#add networkx
import networkx as nx
import random
from matplotlib import pyplot as plt

Graph = nx.Graph()

for nodeNum in range(10):
    Graph.add_node(nodeNum, state = random.randint(0,1), neighborList =[])

# f = open('el_1.txt')
# lines = f.readlines()
# f.close(
# for line in lines:
#     edgeList = line.split()

Graph.add_edge(1, 4)

Graph.node[1]['neighborList'].append(3)
Graph.node[1]['neighborList'].append(4)

neighborList = Graph.node[1]['neighborList']

# print(neighborList)

Graph.add_edge(1, 5)
Graph.add_node(1,neighborNum =5)

list = [2,3,4]
num = random.choice(list)
print num




# print(Graph.nodes(data=True))


# nx.draw(Graph)
# plt.show(Graph)

