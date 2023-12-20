# -*- coding: utf-8 -*-
__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: doublets.py 2023-11-19'

"""
Doublet homework
2023-11
@author:gaspard.torterat-slanda@epita.fr 
"""

from algo_py import graph, queue


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import


#   LEVEL 0
        
def buildgraph(filename, k):
    """Build and return a graph with words of length k from the lexicon in filename

    """
    f = open(filename, 'r')
    L = f.readlines()
    f.close()
    n = len(L) 
    V = []
    p = 0
    for line in range(n):
        if len(L[line]) - 1 == k:
            V.append(L[line][:-1])
            p+=1
    G = graph.Graph(p,False,V);
    for a in range(p):
        for b in range(a,p):
            if a != b:
                cpt = 0
                i = 0
                src = G.labels[a]
                dst = G.labels[b]
                while i < k and cpt < 2:
                    cpt += (src[i] != dst[i])
                    i+=1
                if cpt == 1:
                    G.addedge(a,b)
    return G
###############################################################################
#   LEVEL 1

def mostconnected(G):
    """ Return the list of words that are directly linked to the most other words in G

    """
    MOSTS = []
    _max = 0
    for v in range(G.order):
        tmp = len(G.adjlists[v])
        if tmp > _max:
            _max = tmp
            MOSTS = [G.labels[v]]
        elif tmp == _max:
            MOSTS.append(G.labels[v])
    return MOSTS
        


def ischain(G, L):
    """ Test if L (word list) is a valid elementary *chain* in the graph G

    """
    l = len(L)
    i = 0
    M = [0] * G.order
    _next = L[0]
    for i in range(l-1):
        label = _next
        _next = L[i+1]
        v = 0
        while v < G.order and G.labels[v] != label:
            v+=1
        if v == G.order:
            return False
        if M[v] == 1:
            return False
        else:
            M[v] = 1
        j = 0
        p = len(G.adjlists[v])
        while j < p and G.labels[G.adjlists[v][j]] != _next:
            j+=1
        if j == p:
            return False
    return True 

###############################################################################
#   LEVEL 2

def __dfs(G,x,M,V):
    """ proceed with dfs and adds possible words to V """
    M[x] = 1
    for y in G.adjlists[x]:
        if not M[y]:
            V.append(G.labels[y])
            V = __dfs(G,y,M,V)
    return V
def alldoublets(G, start):
    """ Return the list of all words that can form a *doublet* with the word start in the lexicon in G
    """
    M = [0] * G.order
    v = G.labels.index(start)
    return __dfs(G,v,M,[])

def nosolution(G):
    """ Return a *doublet* without solution in G, (None, None) if none
    
    """
    M = [0] * G.order
    V = __dfs(G,0,M,[])
    i = 0
    for i in range(G.order):
        if not M[i]:
            return (G.labels[0],G.labels[i])
    return (None,None)

###############################################################################
#   LEVEL 3
def __bfs(G,x,end,V):
    """proceeds to bfs and builds the parent vector. Quits when the word end is found.
        returns either the number of the vertex or None if there is no path"""
    V[x] = -1
    Q = queue.Queue()
    Q.enqueue(x)
    while not Q.isempty():
        x = Q.dequeue()
        for y in G.adjlists[x]:
            if V[y] == -2:
                V[y] = x
                if G.labels[y] == end:
                    return y
                else:
                    Q.enqueue(y)
    return None

def ladder(G, start, end):
    """ Return a *ladder* to the *doublet* (start, end) in G
    """
    V = [-2] * G.order
    x = G.labels.index(end)
    v = __bfs(G,x,start,V)
    if v == None:
        return []
    else:
        LAD = []
        while V[v] != -1:
            LAD.append(G.labels[v])
            v = V[v]
        LAD.append(end)
        return LAD 
    
def mostdifficult(G):
    """ Find in G one of the most difficult *doublets* (that has the longest *ladder*)

    """
    start = G.labels[0]
    end = G.labels[0]
    _max = 0
    for a in range(G.order):
        for b in range(a,G.order):
            tmp = len(ladder(G,G.labels[a],G.labels[b]))
            if tmp > _max:
                _max = tmp
                start = G.labels[a]
                end = G.labels[b]
    return (start,end,_max) 

###############################################################################
#   BONUS (just for the fun...)

def isomorphic(G1, G2):
    """BONUS: test if G1 and G2 (graphs of same length words) are isomorphic

    """
    #FIXME
    pass
    
