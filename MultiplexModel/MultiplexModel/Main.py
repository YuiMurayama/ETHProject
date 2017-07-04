# !/usr/bin/python
# coding: UTF-8
#add networkx

import networkx as nx
import random
from gameModel import gameStep, calStrategyNum, makePointList
from opinionModel import opinionExchange, countOpinion
from makeGraph import makeGraph

#ここまでがグラフを作る段階----------------------

#GLの層
divisionNum = 20
gameLayer_info = makeGraph('coordslist1.txt', 'el_1.txt', divisionNum, 'GL')
gameLayer = gameLayer_info[0]
gameLayer_posArray= gameLayer_info[1]
strategyList = gameLayer_info[3]
coopNumList =[]
coopNumList.append(calStrategyNum(gameLayer))

#OLの層
opinionLayer_info = makeGraph('coordslist2.txt', 'el_2.txt', divisionNum, 'ON')
opinionLayer = opinionLayer_info[0]
opinionLayer_posArray= opinionLayer_info[1]
opinionList = opinionLayer_info[2]
# print opinionLayer.node[7]['opinion']
# print opinionLayer.node[12]['opinion']
# print gameLayer.node[12]['strategy']
#-----------------------------------------------ここで二つの層が完成した

#層間の強さ
p_coupling = 0.5

numOfCList_gameLayer =[]
numOfCList_opinionLayer=[]


for num in range(700):
    rand = random.random()
    if rand<p_coupling:    #戦略をコピーする
        p_whichLayer = 0.5     #どちらからどちらへコピーするかの確率
        if random.random()< p_whichLayer:
            #GLからOLにコピー
            for nodeNum in range(nx.number_of_nodes(opinionLayer)):
                opinionLayer.node[nodeNum]['opinion'] = gameLayer.node[nodeNum]['strategy']
        else:
            # OLからGLにコピー
            for nodeNum in range(nx.number_of_nodes(gameLayer)):
                # print opinionLayer[nodeNum]['opinion']
                gameLayer.node[nodeNum]['strategy'] = opinionLayer.node[nodeNum]['opinion']

    else:   #GMとOMがそれぞれ行われる
        gameLayer = gameStep(gameLayer,0.5,0.5)
        numOfCList_gameLayer.append(calStrategyNum(gameLayer))

        G, opinionList = opinionExchange(opinionLayer, opinionList)
        numOfCList_opinionLayer.append(countOpinion(opinionLayer))


print numOfCList_opinionLayer
print numOfCList_gameLayer


# plt.plot(coopNumList)
# plt.xlabel("Time Step")
# plt.ylabel("Number of Cooperators")
#
# plt.show()






# # makePointList(G1)
# print coopNumList
#
# plt.plot(coopNumList)
# plt.xlabel("Time Step")
# plt.ylabel("Number of Cooperators")
#
# plt.show()

#----------------------------------






# pylab.figure(figsize=(8, 8))  # 横3inch 縦4inchのサイズにする
#
# nx.draw_networkx_nodes(G1,G1_posArray, nodelist = [1,2,3], node_size=6, node_color="r")
# nx.draw_networkx_nodes(G1,G1_posArray,nodelist = [4,5,6],node_size=6, node_color="b")
#
# nx.draw_networkx_edges(G1, G1_posArray, width=0.1)
#
# print 'hello'
# pylab.show()
