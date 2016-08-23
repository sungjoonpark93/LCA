__author__ = 'WonhoShin'

import requests
import pandas as pd

def get_berexedges(gene_pairs = None):
    if gene_pairs == None:
        return []
    valid_pairs = []
    gene_set = []
    for g in gene_pairs:
        gene_set.append(g['source'])
        gene_set.append(g['target'])
    gene_set = list(set(gene_set))

    if len(gene_set) == 0:
        return []

    r = requests.get('http://iberex.korea.ac.kr/api/server.php?query=' + '@@'.join(gene_set) + '&mode=1')
    try:
        _json = r.json(strict=False)['data']
    except :
        print "invalid berex query, empty list will be returned"
        return []

    _nodes = _json['nodes']
    _edges = _json['edges']
    edges = {}
    pref = {}
    for e in _nodes:
        pref[e['original']] = e['id']
    for e in _edges:
        if not ((e['source'] + e['target']) in edges):
            edges[e['source'] + e['target']] = []
        _e = {}
        for attr in ['source', 'target', 'interaction', 'dbsource']:
            _e[attr] = e[attr]
        edges[e['source'] + e['target']].append(_e)


    for g in gene_pairs:
        try:
            g1 = pref[g['source']]
            g2 = pref[g['target']]
        except:
            continue

        allowed_db = ['kegg pathway', 'pathwayapi']
        if g1 + g2 in edges:
            for e in edges[g1 + g2]:
                g['interaction'] = e['interaction']
                g['dbsource'] = e['dbsource']
                if g['dbsource'] in allowed_db:
                    valid_pairs.append(g)

    return valid_pairs


def egdelist_to_brexquery(edge_list):
    #edge list is consist of edge tuple
    return [{'source':edge[0],'target':edge[1]} for edge in edge_list]


def berexresult_to_edgelist(berex_result):
    return [(result['source'],result['target'])  for result in berex_result]

if __name__ == "__main__":
    npairs = [{'source':'BRAF', 'target': 'KRAS'}, {'source':'KRAS', 'target': 'BRAF'}, {'source':'EGFR', 'target': 'KRAS'}]
    print npairs
    valid_pairs = get_berexedges(npairs)
    print valid_pairs