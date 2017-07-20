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

    #パイソンのライブラリからグラフを作る
def makeGraph(nodeNum):
    #opinionLayerの作成
    opinionLayer = nx.scale_free_graph(nodeNum)
    # opinionLayer = nx.random_clustered_graph(nodeNum)
    opinionList =[]
    nx.set_node_attributes(opinionLayer, 'opinion',0)

    for nodeNum in range(nx.number_of_nodes(opinionLayer)):
        opinion =random.randint(0, 1)
        opinionLayer.node[nodeNum]['opinion'] = opinion
        opinionList.append(opinion)


    #gameLayerの作成 opinionLayer = nx.random_clustered_graph(nodeNum)
    gameLayer = nx.scale_free_graph(nodeNum)
    # gameLayer = nx.random_clustered_graph(nodeNum)
    nx.set_node_attributes(gameLayer, 'strategy', 0)
    nx.set_node_attributes(gameLayer, 'point', 0)


    strategyList = []
    for nodeNum in range(nx.number_of_nodes(gameLayer)):
        strategy = random.randint(0, 1)
        gameLayer.node[nodeNum]['strategy'] = strategy
        strategyList.append(strategy)
    return opinionLayer,opinionList,gameLayer,strategyList



    #ファイルからグラフを作り出す
def makeGraph_fromFile(coordFile,edgeFile,divisionNum,layer):
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