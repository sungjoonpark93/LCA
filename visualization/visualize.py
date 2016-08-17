__author__ = 'SungJoonPark'
import pandas as pd
from graphviz import Digraph


list1 = [1,2,3,4]
list2 = ['a','b','c']
list3 = ['10','20']

graph = Digraph(format='pdf')
subgraph1 = Digraph()
subgraph2 = Digraph()
subgraph3 = Digraph()

for x in list1:
    subgraph1.node(str(x))
for x in list2:
    subgraph2.node(str(x))

for x in list3:
    subgraph3.node(x)

subgraph1.graph_attr['rank']='same'
subgraph2.graph_attr['rank']='same'
subgraph3.graph_attr['rank']='same'


graph.graph_attr['rankdir']='TB'
graph.subgraph(subgraph1)
graph.subgraph(subgraph2)
graph.subgraph(subgraph3)

graph.edge('1','a')
graph.edge('c','3')
graph.edge('10','1')



graph.view()





