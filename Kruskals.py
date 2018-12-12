# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:12:02 2018

@author: Joseph Wright


Initalize
F = (V(G), 0)

While F is not connected
    add mincost edge not in F (So that F remains a forest)
"""
def Kruskals(edge_file_name,start_vertex = 0):
    G = Weighted_Graph(edge_file_name)
    F = ({G.vertex_set()}, [])
    