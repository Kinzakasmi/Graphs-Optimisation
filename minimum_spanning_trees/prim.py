import networkx as nx
import heapq

def prim(g):
    '''
    Performs Prim's algorithm on a given graph for minimum spanning tree
    Arguments : 
        g : A nx object. The graph to span.
    Returns :
         A dictonary of {node : pred_node}
    '''
    cheapest = {nodes : float("inf") for nodes in g.nodes()}
    pred = {nodes : None for nodes in g.nodes()}
    N = list(g.nodes())

    #init
    s = N[0]
    cheapest[s] = 0
    cheapest_q = []
    heapq.heappush(cheapest_q,(0,s)) #A heap queue to facilitate minimum finding 
    
    while N:
        v = heapq.heappop(cheapest_q)[1]
        if v in N: #If the node has already been visited, continue popping without executing the following
            N.remove(v)
            for n in g.neighbors(v):
                if n in N:
                    if g.get_edge_data(v,n)["weight"] < cheapest[n]:
                        cheapest[n] = g.get_edge_data(v,n)["weight"]
                        heapq.heappush(cheapest_q,(cheapest[n],n))
                        pred[n] = v

    #Reshaping of pred so it returns the same format as the other algorithms
    del pred[list(pred.keys())[0]]
    pred = [(a,b) for (b,a) in pred.items()]           
    return(pred)