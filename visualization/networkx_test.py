__author__ = 'SungJoonPark'

import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
import pydotplus

G = nx.DiGraph()
G.add_node(1,color='blue')
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_edges_from([(1,2),(2,3)])

pos=nx.circular_layout(G)
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='b')
nx.draw_networkx_edges(G,pos,style='dashdot',alpha=0.5,arrows=True,width=10.0)
nx.draw_networkx_labels(G,pos)
write_dot(G,"temp.dot")
plt.show()
