__author__ = 'SungJoonPark'

import pandas as pd
from graphviz import Digraph

def split_list_by_chunk_num(list_, chunk_num):
    #split list by chunk size
    splited_list = []
    bin = len(list_) / chunk_num


    for chunk in range(1,chunk_num+1):
        if chunk == 1:
            splited_list.append(list_[0:bin])
        elif chunk == chunk_num:
            splited_list.append(list_[bin*(chunk-1):])
        else:
            splited_list.append(list_[bin*(chunk-1):(bin*(chunk-1))+bin])
    return splited_list

def get_edge_list_from_adj(adj):
    #get adj matrix and return edge list as list of tuple
    #e.g return [('a','a'),('b','a')]
    return list(adj[adj==1].stack().index)

def get_node_list_from_adj(adj):
    return list(adj.columns)

def arrange(adj_list, chunk_num=4):
    #get input of adj_list and return list of TF node list which the order is considered.

    if len(adj_list)<chunk_num:
        raise Exception('length of adj_list should be larger than chunk_num')
    else:
        splited_adj_list = split_list_by_chunk_num(adj_list,chunk_num)


    graph = Digraph()
    #get node_list from the for adj
    node_list = get_node_list_from_adj(adj_list[0])
    for node in node_list:
        graph.node(node)

    # node_list = get



temp_df = pd.DataFrame([[1,0,0],[1,1,0],[0,0,1]],index=['a','b','c'],columns=['a','b','c'])
print temp_df
print get_edge_list_from_adj(temp_df)
print get_node_list_from_adj(temp_df)