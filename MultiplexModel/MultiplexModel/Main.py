# !/usr/bin/python
# coding: UTF-8
#add networkx

import networkx as nx
import random
from gameModel import gameStep, countC_of_gameLayer, makePointList
from opinionModel import opinionExchange, countC_of_opinionLayer
from makeGraph import makeGraph, makeGraph_fromFile

from matplotlib import pyplot as plt

#ここまでがグラフを作る段階----------------------

#GLの層
divisionNum = 20

gameLayer_info = makeGraph_fromFile('coordslist1.txt', 'el_1.txt', divisionNum, 'GL')
# gameLayer_info = makeGraph_fromFile('coordslist_test.txt', 'edge_test.txt', divisionNum, 'GL')

gameLayer = gameLayer_info[0]
gameLayer_posArray= gameLayer_info[1]
strategyList = gameLayer_info[3]
# coopNumList =[]
# coopNumList.append(countC_of_gameLayer(gameLayer))

#OLの層
opinionLayer_info = makeGraph_fromFile('coordslist2.txt', 'el_2.txt', divisionNum, 'ON')
# opinionLayer_info = makeGraph_fromFile('coordslist_test2.txt', 'edge_test2.txt', divisionNum, 'ON')


opinionLayer = opinionLayer_info[0]
opinionLayer_posArray= opinionLayer_info[1]
opinionList = opinionLayer_info[2]
# print opinionLayer.node[7]['opinion']
# print opinionLayer.node[12]['opinion']
# print gameLayer.node[12]['strategy']
#-----------------------------------------------ここで二つの層が完成した

#---自分で生成したネットワーク
#
# graph = makeGraph(500)
#
# opinionLayer = graph[0]
# opinionList = graph[1]
# gameLayer = graph[2]
# strategyList = graph[3]
#
# print opinionLayer.node[3]['opinion']
# print gameLayer.node[3]['strategy']
#

#-----------------------


#各層のCの数を数えるリスト
numOfCList_gameLayer =[]
numOfCList_opinionLayer=[]

#初期のCooperatorの数をリストに加える
originC_opinionLayer =countC_of_opinionLayer(opinionLayer)
originC_gameLayer =countC_of_gameLayer(gameLayer)


numOfCList_opinionLayer.append(originC_opinionLayer)
numOfCList_gameLayer.append(originC_gameLayer)


#層間の強さ
couplingStrength = 0.0


def printGstate(opinionLayer, gameLayer):
    Gstate_opinion =[]
    Gstate_strategy=[]
    for nodeNum in range(nx.number_of_nodes(opinionLayer)):
        Gstate_opinion.append(opinionLayer.node[nodeNum]['opinion'])
        Gstate_strategy.append(gameLayer.node[nodeNum]['strategy'])

    print "Oは",Gstate_opinion
    # print "Gは",Gstate_strategy



for num in range(300):
    # print num,"番目"８
    # print "前"
    # printGstate(opinionLayer,gameLayer)

    rand = random.random()
    if rand<couplingStrength: #戦略をコピーする
        # print "coupling"
        for nodeNum in range(nx.number_of_nodes(opinionLayer)-1):
            rand_of_whichLayer = random.random()
            # nodeState_gameLayerPre.append(gameLayer.node[nodeNum]['strategy'])
            if rand_of_whichLayer <= 0.5:        #どちらからどちらへコピーするかの確率
                opinionLayer.node[nodeNum]['opinion'] = gameLayer.node[nodeNum]['strategy']

            else:
                gameLayer.node[nodeNum]['strategy'] = opinionLayer.node[nodeNum]['opinion']

        # numOfCList_opinionLayer.append("coupling")
        # numOfCList_gameLayer.append("coupling")
        # printGstate(opinionLayer,gameLayer)


    else:   #GMとOMがそれぞれ行われる
        #GM
        gameLayer = gameStep(gameLayer,0.5,0.5)
        #OM
        opinionLayerset = opinionExchange(opinionLayer, opinionList)
        opinionLayer = opinionLayerset[0]
        opinionList = opinionLayerset[1]
        # G, opinionList = opinionExchange(opinionLayer, opinionList)

        # numOfCList_opinionLayer.append("OL")
        # numOfCList_gameLayer.append("GL")

        # printGstate(opinionLayer,gameLayer)



    # print "後"
    # printGstate(opinionLayer,gameLayer)


    # print ""


    # printGstate_ofOpinion(opinionLayer)
    # print countC_of_opinionLayer(opinionLayer), "を加える"
    #
    # printGstate_ofGame(gameLayer)
    # print countC_of_gameLayer(gameLayer),"を加える"
    # print ""

    numOfCList_gameLayer.append(countC_of_gameLayer(gameLayer))
    numOfCList_opinionLayer.append(countC_of_opinionLayer(opinionLayer))


printGstate(opinionLayer, gameLayer)
# print numOfCList_gameLayer
# print numOfCList_opinionLayer


#グラフの描画
# plt.plot(numOfCList_gameLayer)
plt.plot(numOfCList_opinionLayer)
plt.xlabel("Time Step")
plt.ylabel("Number of Cooperators")

plt.show()



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
