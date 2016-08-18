__author__ = 'SungJoonPark'

import pandas as pd
import random

max_x_pos = 10.0
max_y_pos = 10.0

def get_first_order_node_position(first_adj,node_position):
    first_effected_edges = list(first_adj[first_adj==1].stack().index)
    if len(first_effected_edges)>=1:
        first_effected_source_nodes = [node_tuple[0] for node_tuple in first_effected_edges]
        first_effected_tarted_nodes = [node_tuple[1] for node_tuple in first_effected_edges]
    else:
        raise Exception('No 1 in first adj')


    for i,first_effected_source_node in enumerate(first_effected_source_nodes):
        if first_effected_source_node not in node_position:
            node_position[first_effected_source_node] = tuple([ (i+1)*(max_x_pos / (len(set(first_effected_source_nodes))+1)) ,max_y_pos])

    for i, first_effected_tarted_node in enumerate(first_effected_tarted_nodes):
        if first_effected_tarted_node not in node_position:
            node_position[first_effected_tarted_node] = tuple([ (i+1)*(max_x_pos / len(set(first_effected_tarted_nodes))+1) ,max_y_pos-1])
    return node_position


def get_remaining_node_position(remaining_nodes, node_position):
    for remain_node in remaining_nodes:
        if remain_node not in node_position:
            node_position[remain_node] = (random.uniform(1,8), random.uniform(0,8))
    return node_position


def arragne_node_position(adj_list):
    node_position ={}
    nodes = set(adj_list[0].index)

    #first adj arrange
    first_adj  = adj_list[0]

    node_position = get_first_order_node_position(first_adj,node_position)

    #caculate the remaining nodes
    remaining_nodes = [node for node in nodes if node not in node_position.keys()]

    node_position = get_remaining_node_position(remaining_nodes,node_position)
    return node_position





if __name__ == '__main__':
    adj1 = pd.DataFrame([[0,0,1,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]],index=['a','b','c','d'],columns=['a','b','c','d'])
    adj2 = pd.DataFrame([[0,0,0,1],[0,0,1,0],[1,0,0,0],[0,0,1,0]],index=['a','b','c','d'],columns=['a','b','c','d'])
    adj3 = pd.DataFrame([[0,0,1,0],[0,0,0,1],[1,0,0,0],[1,0,0,0]],index=['a','b','c','d'],columns=['a','b','c','d'])
    adj4 = pd.DataFrame([[0,0,0,1],[1,0,0,0],[0,1,0,0],[1,0,0,0]],index=['a','b','c','d'],columns=['a','b','c','d'])

    adj_list = [adj1, adj2, adj3,adj4]
    print arragne_node_position(adj_list)