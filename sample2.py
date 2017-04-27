# !/usr/bin/python
# coding: UTF-8

#add networkx
import networkx as nx
import random
import sys
from matplotlib import pyplot as plt

G = nx.Graph()
nodeNum = 10

#ノードの生成、 0or1のランダムに意見値、繋がってるノードをリストにいれる
for nodeNum in range(1,nodeNum+1):
    G.add_node(nodeNum, state = random.randint(0,1))


#ファイルから値を取得して、エッジを生成する、近隣ノードのリスト作成
f = open('sample.txt')
lines = f.readlines()
f.close()
for line in lines:
    edgeList = line.split()
    G.add_edge(int(edgeList[0]), int(edgeList[1]))


#print(G.nodes(data=True))



#意見交換のメソッド
def opinionExchange(G):
    exchangeNodeNum = random.randint(1, nx.number_of_nodes(G))#ランダムにノードを選択
    exchangeNode = G.node[exchangeNodeNum]
    # print exchangeNode[nodeNum]

    opponentList = G.neighbors(exchangeNodeNum)
    if opponentList == []:
        print "skip"
        return G
    # print(opponetList)

    opponentNode = G.node[random.choice(opponentList)]#交換相手をリストの中から選択
    # print("pre state",exchangeNode['state'])
    # print("opponet state",opponentNode['state'])
    exchangeNode['state'] = opponentNode['state']#ここで交換する
    # print("after state", exchangeNode['state'])
    # print("opponent", opponentNode['state'])
    return G

def countOpinion(G):
    numOf0 = 0
    numOf1 = 0

    for nodeNum in range(1, nx.number_of_nodes(G) + 1):
        if G.node[nodeNum]['state'] == 0:
            numOf0 += 1

        if G.node[nodeNum]['state'] == 1:
            numOf1 += 1

    print numOf0,"",numOf1




for nodeNum in range(1,nx.number_of_nodes(G)+1):
    print G.node[nodeNum]['state'],
print


for num in range(400):
    G =opinionExchange(G)
    for nodeNum in range(1,nx.number_of_nodes(G)+1):
        print G.node[nodeNum]['state'],
    print
    countOpinion(G)
