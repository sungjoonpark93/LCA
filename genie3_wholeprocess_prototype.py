__author__ = "WonhoShin"
import pandas as pd
import numpy as np
import priorknowledge.berexapi as berex
import inference.genie3 as genie
import visualization.visualize as gviz
import visualization.arrange as arrange

def visualize_genie3_inferenced_res(drug_id=None, start_point = 1, end_point = 20, period = 2, threshold=0.08, overlapping=False):
    s = start_point
    adj_list = []
    fname_list = []

    while s + period <= end_point:
        e = s + period
        rootdir = 'Q:/LCA/data/preprocess_data/06_23/drug_data_observations_merged_TSV'
        adj = genie.run_GENIE3(rootdir, med_num=drug_id, start_point=s, end_point=e, threshold=threshold)
        fname = "./result/GENIE3_th_" + str(threshold) + '/' + str(drug_id) + "/" + str(s) + "_" + str(e)
        adj_list.append(adj)
        fname_list.append(fname)
        if overlapping:
            s += 1
        else:
            s += period

    node_position = arrange.arragne_node_position(adj_list)

    for i in range(len(adj_list)):
        adj = adj_list[i]
        f = fname_list[i]
        gviz.visualize(adj, node_position, outputfile_name=f)

if __name__ == '__main__':
    for drug_id in [1]:
        visualize_genie3_inferenced_res(drug_id = drug_id, start_point = 1, end_point = 20, threshold=0.085, overlapping=True)