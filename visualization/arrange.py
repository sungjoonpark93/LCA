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



def arrange(adj_list, chunk_num=4):
    #get input of adj_list and return list of TF node list which the order is considered.

    if len(adj_list)<4:
        raise Exception('length of adj_list should be larger than chunk_num')



print split_list_by_chunk_num([1,2,3,4,5],4)
