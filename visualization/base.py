__author__ = 'SungJoonPark'
import pandas as pd

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