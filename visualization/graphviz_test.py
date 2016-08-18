__author__ = 'SungJoonPark'
import graphviz as gv


g = gv.Digraph(engine='neato',format='png')
#g.graph_attr['size'] = "10,20!"
g.node('1',pos="0,8!")
g.node('2',pos="3,9!")
g.node('3',pos="8,6!")

g.edge('1','3')
g.edge('3','2')
g.render("temp2.dot",view=False)





