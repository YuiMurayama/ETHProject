# !/usr/bin/python
# coding: UTF-8
#意見交換のメソッド
import networkx as nx
import random
from matplotlib import pyplot as plt
#意見を数えるメソッド
from MultiplexModel.MultiplexModel.makeGraph import makeGraph


def countOpinion(G):
    numOf0 = 0
    numOf1 = 0
    for nodeNum in range(nx.number_of_nodes(G)):
        if G.node[nodeNum]['opinion'] == 0:
            numOf0 += 1
        if G.node[nodeNum]['opinion'] == 1:
            numOf1 += 1
    return numOf0


#意見交換のメソッド
#全てのオピニオンを近隣と交換させる
def opinionExchange(G,opinionList):
    newOpinionList=[]
    for nodeNum in range(nx.number_of_nodes(G)):
        node = G.node[nodeNum]  # ランダムにノードを選択
        copyNode_list = G.neighbors(nodeNum)  # コピー相手の候補リストを作る
        if copyNode_list != []:
            copyNodeNum = random.choice(copyNode_list)  # 候補リストの中からランダムに選択
            # print "copyNodeNum",copyNodeNum
            node['opinion'] = opinionList[copyNodeNum]  # opinionListから戦略をコピー
        newOpinionList.append(node['opinion'])

    opinionList = newOpinionList

    return G,opinionList


# #ここからメイン
# #ノードの生成、 0or1のランダムに意見値、繋がってるノードをリストにいれる、ノードの番号は0~499
# G = nx.Graph()
# nodeNum = 500
# opinionList=[]
#
# for nodeNum in range(nodeNum):
#     opinion = random.randint(0, 1)
#     G.add_node(nodeNum, opinion = opinion)
#     opinionList.append(opinion)
#
# #ファイルを読み込んでエッジの生成
# f = open('el_1.txt')
# lines = f.readlines()
# f.close()
# for line in lines:
#     edgeList = line.split()
#     G.add_edge(int(edgeList[0]), int(edgeList[1]))
#



#ここから試すやつ
# numOf0List =[]
#
# opinionLayer_info = makeGraph('coordslist2.txt', 'el_2.txt', 20, 'ON')
# opinionLayer = opinionLayer_info[0]
# opinionLayer_posArray= opinionLayer_info[1]
# opinionList = opinionLayer_info[2]
#
#
# for num in range(500):
#     G, opinionList = opinionExchange(opinionLayer,opinionList)
#     numOf0 = countOpinion(opinionLayer)
#     numOf0List.append(numOf0)
#
# print numOf0List

# plt.plot(numOf0List)
# plt.xlabel("Time Step")
# plt.ylabel("Number of opinion0")
#
# plt.show()