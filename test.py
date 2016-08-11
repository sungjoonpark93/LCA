__author__ = 'SungJoonPark'

from graphviz import Digraph
dot = Digraph(comment='Thre Round Table')
dot.node('A')
dot.node('B')
dot.node('L')
dot.edges(['AB','AL'])
dot.edge('B','L')
print dot.source
dot.render('test', view=True)