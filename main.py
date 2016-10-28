__author__ = "WonhoShin"
import pandas as pd
import numpy as np
import priorknowledge.berexapi as berex
import inference.genie3 as genie
import inference.tdaracne as td
import visualization.visualize as gviz
import visualization.arrange as arrangea
import visualization.coloring as grad
import argparse

def visualize_genie3_inferenced_res(datadir=None, drug_id=None, start_point = 1, end_point = 20, period = 3, threshold=0.05, overlapping=False):
    s = start_point
    adj_list = []
    fill_info_list = []
    fname_list = []

    while s + period <= end_point:
        e = s + period
        rootdir = 'Q:/LCA/data/preprocess_data/' + datadir + '/drug_data_observations_merged_TSV'
        adj = genie.run_GENIE3(rootdir, med_num=drug_id, start_point=s, end_point=e, cutoff='percentage', threshold=threshold)
        fname = 'Q:/LCA/result/' + datadir + '/GENIE3/period_' + str(period) + '_th_' + str(threshold) + '/' + str(drug_id) + "/" + str(s) + "_" + str(e)
        gradient = grad.run(datadir=datadir, drug_id=drug_id, s=s, e=e)
        adj_list.append(adj)
        fname_list.append(fname)
        fill_info = grad.conv_gradient_to_color(gradient)
        fill_info_list.append(fill_info)
        if overlapping:
            s += 1
        else:
            s += period

    print adj_list
    node_position = arrange.arragne_node_position(adj_list)

    for i in range(len(adj_list)):
        adj = adj_list[i]
        f = fname_list[i]
        fill_info = fill_info_list[i]
        gviz.visualize(adj, node_position, fill_info, outputfile_name=f)

def visualize_tdaracne_inferenced_res(datadir=None, drug_id=None, start_point = 1, end_point = 20, period = 4, overlapping=False):
    s = start_point
    adj_list = []
    fill_info_list = []
    fname_list = []

    while s + period <= end_point:
        e = s + period
        rootdir = 'Q:/LCA/data/preprocess_data/' + datadir + '/drug_data_fill_blank_by_lastobservation/#' + str(drug_id) + '/'
        adj = td.run_TDARACNE(rootdir, start_point=s, end_point=e)
        fname = 'Q:/LCA/result/' + datadir + '/TDARACNE/period_' + str(period) + '/' + str(drug_id) + "/" + str(s) + "_" + str(e)
        gradient = grad.run(datadir=datadir, drug_id=drug_id, s=s, e=e)
        adj_list.append(adj)
        fname_list.append(fname)
        fill_info = grad.conv_gradient_to_color(gradient)
        fill_info_list.append(fill_info)
        if overlapping:
            s += 1
        else:
            s += period

    node_position = arrange.arragne_node_position(adj_list)

    for i in range(len(adj_list)):
        adj = adj_list[i]
        f = fname_list[i]
        fill_info = fill_info_list[i]
        gviz.visualize(adj, node_position, fill_info, outputfile_name=f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--drug-list', type=int, nargs='+', default=[])
    parser.add_argument('--drug-range', type=int, nargs=2, default=[1, 27])
    parser.add_argument('--drug', type=int, default=None)
    parser.add_argument('--time', type=int, default=[1,20], nargs=2)
    parser.add_argument('--period', type=int, default=4)
    parser.add_argument('--genie-th', type=float, default=0.03)
    parser.add_argument('--overlap', dest='overlap', action='store_true', default=True)
    parser.add_argument('--non-overlap', dest='overlap', action='store_false', default=True)
    parser.add_argument('--genie3', dest="method", action="store_const", const="genie3", default="all")
    parser.add_argument('--tdaracne', dest='method', action='store_const', const="tdaracne", default="all")
    parser.add_argument('--datadir', type=str)

    args = parser.parse_args(['--genie3', '--datadir', '06_23', '--drug-range', '1', '1', '--overlap', '--time', '1', '5', '--genie-th', '0.03'])

    drug_list = None

    if len(args.drug_list):
        drug_list = args.drug_list
    elif args.drug != None:
        drug_list = [args.drug]
    else:
        drug_list = range(args.drug_range[0], args.drug_range[1] + 1)

    methods = ['genie3', 'tdaracne']
    if 'all'.startswith(args.method):
        methods = methods
    else:
        methods = [args.method]
    print methods

    # drug_list = ['22']

    for drug_id in drug_list:
         if 'genie3' in methods:
             visualize_genie3_inferenced_res(datadir=args.datadir, drug_id = drug_id, start_point = args.time[0], end_point = args.time[1], threshold=args.genie_th, period=args.period, overlapping=args.overlap)
         if 'tdaracne' in methods:
             visualize_tdaracne_inferenced_res(datadir=args.datadir, drug_id=drug_id, start_point=args.time[0], end_point=args.time[1], period=args.period, overlapping=args.overlap)