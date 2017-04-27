# !/usr/bin/python
# coding: UTF-8

#add networkx
import networkx as nx
import random
import sys
from matplotlib import pyplot as plt

Graph = nx.Graph()

#ノードの生成、 0or1のランダムに意見値、繋がってるノードをリストにいれる
for nodeNum in range(11):
    Graph.add_node(nodeNum, state = random.randint(0,1), neighborList=[])


#ファイルから値を取得して、エッジを生成する、近隣ノードのリスト作成
f = open('sample.txt')
lines = f.readlines()
f.close()
for line in lines:
    edgeList = line.split()
    Graph.add_edge(int(edgeList[0]), int(edgeList[1]))
    Graph.node[int(edgeList[0])]['neighborList'].append(int(edgeList[1]))

#print(Graph.nodes(data=True))



#意見交換のメソッド
def opinionExchange(G,nodeNum):
    exchangeNode = G.node[random.randint(0, nodeNum-1)]#ランダムにノードを選択
    # print exchangeNode[nodeNum]
    opponetList = exchangeNode['neighborList']
    if opponetList == []:
        print "skip"
        return G
    # print(opponetList)

    opponentNode = G.node[random.choice(opponetList)]#交換相手をリストの中から選択
    print("pre state",exchangeNode['state'])
    # print("opponet state",opponentNode['state'])
    exchangeNode['state'] = opponentNode['state']#ここで交換する
    print("after state", exchangeNode['state'])
    # print("opponent", opponentNode['state'])

    return G


for nodeNum in range(11):
    print Graph.node[nodeNum]['state'],
print


for num in range(11):
    Graph =opinionExchange(Graph,11)
    for nodeNum in range(11):
        print Graph.node[nodeNum]['state'],
    print
