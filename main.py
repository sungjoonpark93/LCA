__author__ = 'SungJoonPark'
import pandas as pd
import inference

inputfile =""

for drug in drugs:
    for time_point in time_points:
        inference_network = inference(time_point_data, algorithm='')
        priorknowledge_edges = search_priorknowledge_edges(inference_network)
        visualize(inference_network,priorknowledge_edges,is_priorknowledge=False)