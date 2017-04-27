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
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import pylab

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

#区画ごとの数を数えて区画ごとのパーセンテージリストを返すメソッド
def countNumOfNodesByDivision(G,divisionNum):
    divisionNumOf0 =np.array([0]*divisionNum)
    divisionNumof1 =np.array([0]*divisionNum)
    divisionNumPercent =np.array([0.0]*divisionNum)

    for nodeNum in range(nx.number_of_nodes(G)):
        if(int(G.node[nodeNum]['state']) == 0):
            divisionNumOf0[int(G.node[nodeNum]['district'])] += 1
        else:
            divisionNumof1[int(G.node[nodeNum]['district'])] += 1
    # print divisionNumOf0
    # print divisionNumof1

    for i in range(divisionNum):
        if (divisionNumOf0[i]+divisionNumof1[i] == 0):
            divisionNumPercent[i]=0
        else:
            divisionNumPercent[i] = (divisionNumOf0[i]*1.0)/(divisionNumOf0[i]+divisionNumof1[i])
        # print int(G.node[nodeNum]['division'])
    # print "percent",divisionNumPercent
    return divisionNumPercent

#なんか描画するやつ
def draw_heatmap(data, row_labels, column_labels):
    # 描画する
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(data, cmap=plt.cm.Blues)

    ax.set_yticks(np.arange(data.shape[0]*0.3) + 0.5, minor=False)
    ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)

    print data.shape[0]
    print data.shape[1]
    ax.set_xlabel('Angular Bin')
    ax.set_ylabel('Time Step')

    ax.invert_yaxis()
    ax.xaxis.tick_top()

    ax.set_xticklabels(column_labels, minor=False)
    ax.set_yticklabels(row_labels, minor=False)
    plt.show()
    plt.savefig('image.png')

    return heatmap


#ここからがメイン
#ファイルを読み込んで、ノード作成、座標の設定、state生成、ノードの番号は0~499
G = nx.Graph()
f_coords = open('coords.txt')
coordsLines = f_coords.readlines()
f_coords.close()

divisionNum =20
between = 2*math.pi/divisionNum

for line in coordsLines:
    # print line
    coordList = line.split()
    # print coordList
    r = float(coordList[2])
    t = float(coordList[1])
    G.add_node(int(coordList[0]),pos=(r*math.cos(t),r*math.sin(t)),state=random.randint(0, 1),district =t//between)

countNumOfNodesByDivision(G,divisionNum)

#ファイルを読み込んでエッジの生成
f_edge = open('el_1.txt')
edgeLines = f_edge.readlines()
f_edge.close()
for line in edgeLines:
    edgeList = line.split()
    G.add_edge(int(edgeList[0]), int(edgeList[1]))


# print G.nodes(data=True)
#グラフを描画する部分
# plt.figure(figsize=(5,5))
# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G, pos, node_color="w",alpha=0.6, node_size=5)
# plt.show()

#意見交換させる
exchangeNum = 180000
districtRateList =np.zeros([0,divisionNum])
# districtRateList =np.zeros([divisionNum,0])

opinionList =[]
for num in range(exchangeNum):
    #意見交換
    G =opinionExchange(G)
    # 最初と最後だけ
    # if num == 0  or num == exchangeNum-1:
    if num% 1000 == 0:
        # countNumOfNodesByDivision(G, divisionNum)
        # numOf0 = countOpinion(G)
        # districtRateList[num]=countNumOfNodesByDivision(G,divisionNum)
        districtRateList=np.r_[districtRateList,countNumOfNodesByDivision(G,divisionNum).reshape(1,-1)]
        numOf0 = countOpinion(G)
        opinionList.append(numOf0)
    # if num == exchangeNum-1:
    #     print opinionList

# print districtRateList



#ヒートマップ
# draw_heatmap(districtRateList, "step", "bin")

#グラフの描画

pylab.figure(figsize=(6, 8))  # 横3inch 縦4inchのサイズにする
pos = nx.spring_layout(G)  # いい感じにplotする

nx.draw_networkx_nodes(G, pos, node_size=1, node_color="w")
nx.draw_networkx_edges(G, pos, width=0.1)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# nx.draw_networkx_labels(G, pos, font_size=16, font_color="r")


pylab.xticks([])
pylab.yticks([])

pylab.show()


# plt.imshow(districtRateList)
# plt.show()

# df_data = sns.load_dataset(districtRateList)
# sns.heatmap(df_data)


# print districtRateList
#
# #csvに書き込む
f = open('result2.csv', 'w')
writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
writer.writerows(districtRateList)     # list（1次元配列）の場合
f.close()