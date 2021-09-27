# UnionFind structures
from copy import copy
import networkx as nx

class PointedStructure():
    ''' Class that resembles pointers in C'''
    def __init__(self,n):
        self.pred = None
        self.name = n
        
    def add(self,n):
        self.pred = n
        
    def head(self):
        while self.pred != None :
            self = self.pred
        return(self)

class UnionFind():
    def __init__(self,nodes):
        self.subsets = {}
        for n in nodes :
            self.subsets[n] = PointedStructure(n)
    
    def find(self,u):
        for (_,subset) in self.subsets.items() :
            c = copy(subset)
            while (not (c.pred is None)) and (c.name != u) :
                c = c.pred
            if c.name == u :
                return(subset.head())
        return(None)
    
    def union(self,u,v):
        head_u = self.find(u)
        head_v = self.find(v)
        head_u.pred = head_v

def kruskal(g):
    '''Performs Kruskal's algorithm for minimum spanning trees
    Arguments : 
        g : A nx object. The graph to span.
    Returns :
        A  list of (pred_node,node)
    '''
    import heapq
    edges = [(g.get_edge_data(*edge)["weight"], edge) for edge in g.edges()]
    heapq.heapify(edges)
    mst = []
    unionFind = UnionFind(list(g.nodes()))
    while edges != [] :
        u,v = edges[0][1]
        heapq.heappop(edges)
        if unionFind.find(u) != unionFind.find(v) :
            unionFind.union(u,v)
            mst.append((u,v))
    return mst

if __name__ == '__main__' :
    # Initialize graph
    g = nx.Graph()
    g.add_node("A", pos=(1,2))
    g.add_node("B", pos=(0,1))
    g.add_node("C", pos=(2,1))
    g.add_node("D", pos=(2,0))
    g.add_weighted_edges_from([["A", "B", 3], ["A", "C", 1], ["C", "B", 1], ["C", "D", 3], ["D", "B", 1]])

    # Test pointed structures
    a = PointedStructure("A")
    assert(a.pred is None)
    b = PointedStructure("B")
    c = PointedStructure("C")
    d = PointedStructure("D")
    a.add(b)
    b.add(c)
    d.add(a)
    assert(a.head().name == 'C')   

    # Test UnionFind
    union = UnionFind(["A","B","C","D","E", "F"])
    union.union("A","B")
    union.union("C","A")
    union.union("D","B")

    assert(union.find("A").name == 'B')
    assert(union.find("B").name == 'B')

    union.union("B","E")

    assert(union.find("A").name == 'E')
    assert(union.find("B").name == 'E')
    assert(union.find("E").name == 'E')
    assert(union.find("D") == union.find("E"))
    assert(union.find("F") != union.find("E"))  

    #Test Kruskal algorithm
    assert(kruskal(g) == [('A','C'),('B','C'),('B','D')])             
