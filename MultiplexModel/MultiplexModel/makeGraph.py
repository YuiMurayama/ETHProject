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
def makeGraph(coordFile,edgeFile,divisionNum,layer):
    G = nx.Graph()
    f_coords = open(coordFile)
    coordsLines = f_coords.readlines()
    f_coords.close()
    between = 2 * math.pi / divisionNum
    pos_array = []

    opinionList =[]
    strategyList =[]

    for line in coordsLines:
        coordList = line.split()
        t = float(coordList[2])
        r = float(coordList[3])
        # print t
        pos_array.append([r * math.cos(t), r * math.sin(t)])

        #opinionModelなら座標と0か1の意見をもたせる
        if layer == 'ON':
            opinion = random.randint(0, 1)
            G.add_node(int(coordList[1]), opinion=opinion, district=t // between)
            opinionList.append(opinion)

        #gameModelなら座標と0か1の戦略をもたせる
        else:
            strategy = random.randint(0,1)
            G.add_node(int(coordList[1]), point=0, district=t // between, strategy=strategy)#0がcooperation,1がDefection
            strategyList.append(strategy)


    f_edge = open(edgeFile)
    edgeLines = f_edge.readlines()
    f_edge.close()
    for line in edgeLines:
        edgeList = line.split()
        G.add_edge(int(edgeList[0]), int(edgeList[1]))

    #Gと座標のリストをかえす

    # print pos_array

    return(G,pos_array,opinionList,strategyList)