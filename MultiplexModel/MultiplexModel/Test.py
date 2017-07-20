# !/usr/bin/python
# coding: UTF-8
#add networkx
import math
import networkx as nx
import random
import sys
import csv
import matplotlib.pyplot as plt
#pandasと相性がいい
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import pylab


G = nx.scale_free_graph(10)
nx.set_node_attributes(G, 'opinion',0)


for nodeNum in range(nx.number_of_nodes(G)):
    G.node[nodeNum]['opinion'] =random.randint(0, 1)



print G.node[0]['opinion'],G.node[1]['opinion'],G.node[2]['opinion'],G.node[3]['opinion'],G.node[4]['opinion'],





# plt.plot(coopNumList)
# plt.xlabel("Time Step")
# plt.ylabel("Number of Cooperator")
#
# plt.show()

