__author__ = 'SungJoonPark'
import pandas as pd
import graphviz as gv
import arrange
import base
import priorknowledge.berexapi as berex

def tuple_to_pos(node_tuple):
    return str(node_tuple[0])+","+str(node_tuple[1])+"!"


def visualize(adj,node_position, fill_info, outputfile_name=None):
    g = gv.Digraph(engine='neato',format='png')
    g.graph_attr['overlap']='false'
    g.graph_attr['splines'] = 'true'
    #g.graph_attr['sep'] = '1'
    #g.graph_attr['esep'] = '0.7'
    #g.graph_attr['splines'] = 'ortho'
    #g.graph_attr['inputscale'] = '5'
    #g.graph_attr['size']='30!'
    #g.graph_attr['ratio'] = 'expand'
    #put node information in graph object
    print node_position
    print fill_info
    for node in node_position.keys():
        g.node(node,pos=tuple_to_pos(node_position[node]), style="filled", color=fill_info[node])

    #get edge information
    inference_edge_list = base.get_edge_list_from_adj(adj)
    berex_edge_list = berex.berexresult_to_edgelist(berex.get_berexedges(berex.egdelist_to_brexquery(inference_edge_list)))

    only_inference_edge_list=list(set(inference_edge_list).difference(set(berex_edge_list)))
    both_edge_list = berex_edge_list

    #put edge information to graphic object
    #only inference
    for edge in only_inference_edge_list:
        g.edge(edge[0],edge[1],style='dashed')
    #both edges
    for edge in both_edge_list:
        g.edge(edge[0],edge[1])


    #node coloring

    g.render(filename=outputfile_name,view=False)

if __name__ =='__main__':
    adj1 = pd.DataFrame([[0,0,1,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]],index=['a','b','c','d'],columns=['a','b','c','d'])
    adj2 = pd.DataFrame([[0,0,0,1],[0,0,1,0],[1,0,0,0],[0,0,1,0]],index=['a','b','c','d'],columns=['a','b','c','d'])
    adj3 = pd.DataFrame([[0,0,1,0],[0,0,0,1],[1,0,0,0],[1,0,0,0]],index=['a','b','c','d'],columns=['a','b','c','d'])
    adj4 = pd.DataFrame([[0,0,0,1],[1,0,0,0],[0,1,0,0],[1,0,0,0]],index=['a','b','c','d'],columns=['a','b','c','d'])

    adj_list = [adj1, adj2, adj3, adj4]
    node_position = arrange.arragne_node_position(adj_list)
    visualize(adj_list[0], node_position,outputfile_name="./result/temp1")
    #visualize(adj_list[1], node_position,outputfile_name="./result/temp2")