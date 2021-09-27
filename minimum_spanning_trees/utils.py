import networkx as nx
import matplotlib.pyplot as plt

def plot_solution(solution) :
    ''' Plots the solution graph'''
    g_solution = nx.DiGraph()
    g_solution.add_edges_from(solution)

    plot_graph(g_solution)
    return g_solution

def plot_graph(g):
    '''Plots a networkx graph'''
    
    ax = plt.axes()
    ax.set_axis_off()
    ax.set_aspect(1)
    
    pos = nx.get_node_attributes(g,"pos")
    if pos == {} :
        #pos = nx.spring_layout(g) # pos = nx.nx_agraph.graphviz_layout(G)
        pos = nx.shell_layout(g)
    nx.draw_networkx(g,pos)
    labels = nx.get_edge_attributes(g,'weight')
    nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)