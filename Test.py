import numpy as np
import matplotlib.pyplot as plt
import multinetx as mx


N = 10
g1 = mx.erdos_renyi_graph(N,0.07,seed=218)
g2 = mx.erdos_renyi_graph(N,0.07,seed=211)


adj_block = mx.lil_matrix(np.zeros((N*2,N*2)))

adj_block[0:  N,  N:2*N] = np.identity(N)    # L_12
adj_block += adj_block.T

mg = mx.MultilayerGraph(list_of_layers=[g1,g2],inter_adjacency_matrix=adj_block)
mg.set_edges_weights(inter_layer_edges_weight=2)

mg.set_intra_edges_weights(layer=0,weight=1)
mg.set_intra_edges_weights(layer=1,weight=2)

fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(122)
ax1.axis('off')
ax1.set_title('regular interconnected network')
pos = mx.get_position(mg,mx.fruchterman_reingold_layout(mg.get_layer(0)),
					  layer_vertical_shift=1.4,
					  layer_horizontal_shift=0.0,
					  proj_angle=7)

mx.draw_networkx(mg, pos=pos, ax=ax1, node_size=30, with_labels=False,
				 edge_color=[mg[a][b]['weight'] for a,b in mg.edges()],
				 edge_cmap=plt.cm.jet_r)

plt.show()




# print(numpy.__file__)

