__author__ = 'SungJoonPark'
import pandas as pd
import graphviz as gv
import arrange
import base
import priorknowledge.berexapi as berex

def tuple_to_pos(node_tuple):
    return str(node_tuple[0])+","+str(node_tuple[1])+"!"


def visualize(adj,node_position, outputfile_name=None):
    g = gv.Digraph(engine='neato',format='png')

    #put node information in graph object
    for node in node_position.keys():
        g.node(node,pos=tuple_to_pos(node_position[node]))

    #put edge information in graph object
    #first, from inference
    edge_list = base.get_edge_list_from_adj(adj)
    for edge in edge_list:
        g.edge(edge[0],edge[1])

    #second, from berex
    #get berex edge from infrence edge list
    berex_edge_list = berex.berexresult_to_edgelist(berex.egdelist_to_brexquery(edge_list))
    print berex_edge_list

    #arrow shaping

    #node coloring

    g.render(filename="result/temp",view=False)

if __name__ =='__main__':
    adj1 = pd.DataFrame([[0,0,1,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]],index=['a','b','c','d'],columns=['a','b','c','d'])
    adj2 = pd.DataFrame([[0,0,0,1],[0,0,1,0],[1,0,0,0],[0,0,1,0]],index=['a','b','c','d'],columns=['a','b','c','d'])
    adj3 = pd.DataFrame([[0,0,1,0],[0,0,0,1],[1,0,0,0],[1,0,0,0]],index=['a','b','c','d'],columns=['a','b','c','d'])
    adj4 = pd.DataFrame([[0,0,0,1],[1,0,0,0],[0,1,0,0],[1,0,0,0]],index=['a','b','c','d'],columns=['a','b','c','d'])

    adj_list = [adj1, adj2, adj3, adj4]
    node_position = arrange.arragne_node_position(adj_list)
    visualize(adj_list[0], node_position)