# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:36:35 2018

@author: Joseph Wright
"""
from Weighted_Graph import Weighted_Graph
from functions import update, total_sum


def Prims(edge_file_name, start_vertex = 0, draw = False):
    T = ({start_vertex}, [])
    G = Weighted_Graph(edge_file_name)
    if draw == True:
        G.draw_graph()
    while T[0] != G.vertex_set():
        T = update(T,G)
        G.draw_subgraph(T)
    print("The minimum spanning tree costs: " +str(total_sum(T,G)))
    return T

