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

#囚人のジレンマゲーム
def game(G, s, t):
    strategyList = []
    for nodeNum in range(nx.number_of_nodes(G)):
        p1 = G.node[nodeNum]#ランダムにノードを選択
        p2_list =G.neighbors(nodeNum)
        if p2_list != []:
            p2 = G.node[random.choice(p2_list)]
            if p1['strategy'] == 0 and p2['strategy'] == 0:
                p1['point'] += 1
                p2['point'] += 1
            elif p1['strategy'] == 0 and p2['strategy'] == 1:
                p1['point'] += s
                p2['point'] += t
            elif p1['strategy'] == 1 and p2['strategy'] == 0:
                p1['point'] += t
                p2['point'] += s
            else:
                p1['point'] += 0
                p2['point'] += 0
        strategyList.append(p1['strategy'])
    return G,strategyList


def makePointList(G):
    pointList =[]
    for nodeNum in range(nx.number_of_nodes(G)):
        pointList.append(G.node[nodeNum]['point'])
    print pointList
    return pointList



#戦略をコピーする
def copyStrategy(G,strategyList):
    for nodeNum in range(nx.number_of_nodes(G)):
        node = G.node[nodeNum]  # ランダムにノードを選択
        copyNode_list = G.neighbors(nodeNum)
        if copyNode_list != []:
            copyNodeNum =random.choice(copyNode_list)
            copyNode = G.node[copyNodeNum]
            p = (1.0-math.tanh(node['point']-copyNode['point']))*0.5
            # print 'tanh', math.tanh(node['point'] - copyNode['point']),'pは',p
            x = random.random()
            if x < p:
                node['strategy'] = strategyList[copyNodeNum]            # print 'exchange'
        node['point'] = 0#全てのポイントをリセットする

    return G


#CとDの数を数える
def calStrategyNum(G):
    nodeNumArrayOfC =[]
    nodeNumArrayOfD =[]
    numOfCooperator = 0
    numOfDefector = 0
    for nodeNum in range(nx.number_of_nodes(G)):
        if G.node[nodeNum]['strategy'] == 0:
            numOfCooperator += 1
            nodeNumArrayOfC.append(nodeNum)
        if G.node[nodeNum]['strategy'] == 1:
            numOfDefector += 1
            nodeNumArrayOfD.append(nodeNum)
    return numOfCooperator
    # return (nodeNumArrayOfC,nodeNumArrayOfD)



def gameStep(G,s,t):
    G = game(G,s,t)[0]
    strategyList = game(G,s,t)[1]
    G =copyStrategy(G,strategyList)
    # print calStrategyNum(G)
    return G