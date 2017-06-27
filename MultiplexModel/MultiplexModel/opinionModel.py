# !/usr/bin/python
# coding: UTF-8
#意見交換のメソッド
import random
import networkx as nx
import random
import sys
import csv
import numpy as np


from matplotlib import pyplot as plt



#意見を数えるメソッド
def countOpinion(G):
    opinionArray =[]
    numOf0 = 0
    numOf1 = 0
    for nodeNum in range(nx.number_of_nodes(G)):
        if G.node[nodeNum]['opinion'] == 0:
            numOf0 += 1
        if G.node[nodeNum]['opinion'] == 1:
            numOf1 += 1
    return numOf0


#意見交換のメソッド
def opinionExchange(G,opinionList):
    newOpinionList=[]
    for nodeNum in range(nx.number_of_nodes(G)):
        node = G.node[nodeNum]  # ランダムにノードを選択
        copyNode_list = G.neighbors(nodeNum)  # コピー相手の候補リストを作る
        if copyNode_list != []:
            copyNodeNum = random.choice(copyNode_list)  # 候補リストの中からランダムに選択
            copyNode = G.node[copyNodeNum]  # コピー相手の決定
            node['opinion'] = opinionList[copyNodeNum]  # opinionListから戦略をコピー

        newOpinionList.append(node['opinion'])

    opinionList = newOpinionList
    return G,opinionList







#ここからメイン
#ノードの生成、 0or1のランダムに意見値、繋がってるノードをリストにいれる、ノードの番号は0~499
G = nx.Graph()
nodeNum = 500
opinionList=[]

for nodeNum in range(nodeNum):
    opinion = random.randint(0, 1)
    G.add_node(nodeNum, opinion = opinion)
    opinionList.append(opinion)



#ファイルを読み込んでエッジの生成
f = open('el_1.txt')
lines = f.readlines()
f.close()
for line in lines:
    edgeList = line.split()
    G.add_edge(int(edgeList[0]), int(edgeList[1]))

numOf0List =[]

for num in range(0,500):
    Gset = opinionExchange(G,opinionList)
    G =Gset[0]
    opinionList = Gset[1]
    numOf0 = countOpinion(G)

    numOf0List.append(numOf0)

    # opinionList.append(numOf0)


print numOf0List




# plt.plot(opinionList)
# plt.xlabel("Time Step")
# plt.ylabel("Number of opinion0")
#
# plt.show()
