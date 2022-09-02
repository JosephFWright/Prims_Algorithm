# -*- coding: utf-8 -*-
"""
Functions that perform manipulation on Weighted_Graph.py for Prims/Kruskals*
MST problem.


"""

from Weighted_Graph import *

G = Weighted_Graph('test_graph.txt')

""" This function determines the cost(c) of a edge that is received against the
    graph file """
def c(e,G):
    return G.edge_dict()[e]

""" Incident Edges will return all possible edges that can be in the tree""" 
def incident_edges(T,G):
    edges = []
    for v in T[0]:
        for e in G.edge_set():
            if v in e and e not in edges:
                edges.append(e)
        for e in edges:
            if e in T[1]:
                edges.remove(e)          
    return edges

""" Valid Edges checks the edges from Incident edges to make sure none will
    create a cycle within the tree: removes edges that do """
def valid_edges(T, G):
    edges = incident_edges(T,G)
    notvalid = incident_edges(T,G)
    vlist = G.vertex_set().difference(set(T[0]))
    for v in T[0]:
        for x in vlist:
            for e in G.edge_set():
                if v in e and x in e and e in edges:
                    notvalid.remove(e)
    edges = list(set(edges) - set(notvalid))
    return edges      

""" From Valid Edges, minimum valid edges will return the cheapest edge that
    continues the MST"""
def min_valid_edges(T,G):
    edges = valid_edges(T, G)
    min_edges = edges[0]     
    for e in edges:
        if (c(e,G)) < c(min_edges,G):
            min_edges = e
    return min_edges

""" Update will take the tuple of vertices and edges and update it with the
    newly found edge """
def update(T,G):
    vertices = set(T[0])
    edges = list(T[1])
    update = min_valid_edges(T,G)
    edges.append(update)
    for v in update:
        if v in G.vertex_set() and v not in vertices:
            vertices.add(v)
    T2 = [vertices, edges]
    return T2

"""
    Calculates the final cost of all the edges in the tree """
def total_sum(T, G):
    return sum([c(e,G) for e in T[1]])