__author__ = 'SungJoonPark'
import graphviz as gv

g = gv.Digraph(engine='neato',format='png')

g.node('1',pos="0,0.5!")
g.node('2',pos="0.5,1!")
g.node('3',pos="1,0!")


g.render("temp2.dot",view=False)
