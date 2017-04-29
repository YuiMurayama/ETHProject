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


def gameModel(G,s,t):
    p1 = G.node[random.randint(0, nx.number_of_nodes(G)-1)]#ランダムにノードを選択
    p2 = G.node[random.choice(G.neighbors(G.node[p1]))]
    p1_str = 'C'
    p2_str = 'D'

    if p1_str == 'C' and p2_str == 'C':
        p1['point'] += 1
        p2['point'] += 1
    elif p1_str == 'C' and p2_str == 'D':
        p1['point'] += s
        p2['point'] += t
    elif  p1_str == 'D' and p2_str == 'S':
        p1['point'] += t
        p2['point'] += s
    else:
        p1['point'] += 0
        p2['point'] += 0












    return G


def opinionExchange(G):
    exchangeNodeNum = random.randint(0, nx.number_of_nodes(G)-1)#ランダムにノードを選択
    exchangeNode = G.node[exchangeNodeNum]
    opponentList = G.neighbors(exchangeNodeNum)
    if opponentList == []:
        # print "skip"
        return G
    opponentNode = G.node[random.choice(opponentList)]#交換相手をリストの中から選択
    exchangeNode['state'] = opponentNode['state']#ここで交換する
    # print("after state", exchangeNode['state'])
    # print("opponent", opponentNode['state'])
    return G


