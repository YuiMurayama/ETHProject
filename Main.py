# !/usr/bin/python
# coding: UTF-8
#add networkx
import networkx as nx
import random
import sys
import csv
import numpy as np


from matplotlib import pyplot as plt

#意見交換のメソッド
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
#意見を数えるメソッド
def countOpinion(G):
    opinionArray =[]
    numOf0 = 0
    numOf1 = 0
    for nodeNum in range(nx.number_of_nodes(G)):
        if G.node[nodeNum]['state'] == 0:
            numOf0 += 1
        if G.node[nodeNum]['state'] == 1:
            numOf1 += 1
    return numOf0


#ここからメイン
#ノードの生成、 0or1のランダムに意見値、繋がってるノードをリストにいれる、ノードの番号は0~499
G = nx.Graph()
nodeNum = 448
for nodeNum in range(nodeNum):
    G.add_node(nodeNum, state = random.randint(0,1))

#ファイルを読み込んでエッジの生成
f = open('el_new_12_4.txt')
lines = f.readlines()
f.close()
for line in lines:
    edgeList = line.split()
    G.add_edge(int(edgeList[0]), int(edgeList[1]))

#意見交換させる
opinionList =[]
for num in range(150000):
    G =opinionExchange(G)
    if num %100 == 0:
        numOf0 = countOpinion(G)
        opinionList.append(numOf0)
print opinionList

#csvに書き込む
# f = open('result3.csv', 'w')
# writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
# writer.writerow(opinionList)     # list（1次元配列）の場合
# f.close()

#描画する
# x = np.arange(0,500,10)
# x = opinionList
# y= numOf0

# x = np.arange(-3, 3, 0.1)
y = opinionList
print y
plt.plot(y)
plt.show()