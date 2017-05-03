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

from MultiplexModel.MultiplexModel.Gamemodel import gameStep, calStrategyNum, makePointList
from MultiplexModel.MultiplexModel.makeGraph import makeGraph

divisionNum = 20
G1_info = makeGraph('coordslist1.txt','el_1.txt',divisionNum,'GN')
G1 = G1_info[0]
G1_posArray= G1_info[1]

coopNumList =[]
coopNumList.append(calStrategyNum(G1))

for num in range(100):
    gameStep(G1,0.5,0.5)
    if num % 1 == 0:
        coopNumList.append(calStrategyNum(G1))

# makePointList(G1)
print coopNumList

plt.plot(coopNumList)
plt.xlabel("Time Step")
plt.ylabel("Number of Cooperators")

plt.show()


# pylab.figure(figsize=(8, 8))  # 横3inch 縦4inchのサイズにする
#
# nx.draw_networkx_nodes(G1,G1_posArray, nodelist = [1,2,3], node_size=6, node_color="r")
# nx.draw_networkx_nodes(G1,G1_posArray,nodelist = [4,5,6],node_size=6, node_color="b")
#
# nx.draw_networkx_edges(G1, G1_posArray, width=0.1)
#
# print 'hello'
# pylab.show()
