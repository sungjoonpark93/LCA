__author__ = "WonhoShin"

import csv
from scipy.optimize import curve_fit

def curve_f(x, A, B):
    return A * x + B

def compute_bestfit_gradient(datadir=None, drug_id=None, s=None, e=None):
    rootdir = 'Q:/LCA/data/preprocess_data/' + datadir + '/drug_data_observations_merged_TSV/'
    fpath = rootdir + str(drug_id) + '.tsv'
    file = open(fpath, 'rb')
    data = csv.reader(file, delimiter='\t')
    table = [row for row in data]
    print table

    gradient = {}

    X = range(s, e + 1)

    for i, row in enumerate(table):
        if i == 0:
            continue
        _y = row[s : e + 1]
        y = [float(x) for x in _y]
        A, B = curve_fit(curve_f, X, y)[0]
        gradient[row[0]] = A
    return gradient

def conv_gradient_to_color(gradient):
    color_set = {}

    # continuous color table
    # for k in gradient:
    #     g = gradient[k]
    #     if g > 0:
    #         g = min(g, 5.0)
    #         color_set[k] = '#FF' + '{0:02x}'.format(255 - int(51 * g)) + '55'
    #     else:
    #         g = max(g, -5.0)
    #         color_set[k] = '#' + '{0:02x}'.format(255 - int(51 * (-g))) + 'FF55'

    palette = [[4.0, '#FF0055'], [1.0, '#FF9955'], [-1.0, '#FFFF55'], [-4.0, '#99FF55'], [-1000000.0, '#00FF55']]

    for k in gradient:
        g = gradient[k]
        for picked in palette:
            if g >= picked[0] or picked[1] == palette[-1][1]:
                color_set[k] = picked[1]
                break

    return color_set

def run(datadir=None, drug_id=None, s=None, e=None):
    return compute_bestfit_gradient(datadir=datadir, drug_id=drug_id, s=s, e=e)


if __name__ == '__main__':
    compute_bestfit_gradient(drug_id=1, s=1, e=5)