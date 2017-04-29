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


#グラフを作り出す部分
def makeGraph(coordFile,edgeFile,divisionNum):
    G = nx.Graph()
    f_coords = open(coordFile)
    coordsLines = f_coords.readlines()
    f_coords.close()
    between = 2 * math.pi / divisionNum
    pos_array = []
    for line in coordsLines:
        coordList = line.split()
        t = float(coordList[2])
        r = float(coordList[3])
        # print t
        G.add_node(int(coordList[1]), state=random.randint(0, 1), district=t // between)
        pos_array.append([r * math.cos(t), r * math.sin(t)])

    f_edge = open(edgeFile)
    edgeLines = f_edge.readlines()
    f_edge.close()
    for line in edgeLines:
        edgeList = line.split()
        G.add_edge(int(edgeList[0]), int(edgeList[1]))

    return (G,pos_array)

divisionNum = 20
G1_info = makeGraph('coordslist1.txt','el_1.txt',divisionNum)
G1 = G1_info[0]
G1_posArray= G1_info[1]


pylab.figure(figsize=(8, 8))  # 横3inch 縦4inchのサイズにする

nx.draw_networkx_nodes(G1,G1_posArray, nodelist = [1,2,3], node_size=6, node_color="r")
nx.draw_networkx_nodes(G1,G1_posArray,nodelist = [4,5,6],node_size=6, node_color="b")

nx.draw_networkx_edges(G1, G1_posArray, width=0.1)

pylab.show()
