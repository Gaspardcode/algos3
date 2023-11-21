from queue import *
from stack import *
from graph import *
from graphmat import *
from ex import *

def degrees(G):
    V = []
    for L in G.adj:
        d=0
        for i in L:
            d+=i
        V.append(d)
    return V

def in_out_degrees(G):
    IN,OUT = [],[]
    for L in G.adjlists:
        d_out = 0
        for i in L:
            d_out +=1
        OUT.append(d_out)
    for s in range(G.order):
        d_in = 0
        for L in G.adjlists:
            for i in L:
                if(i==s):
                    d_in+=1
        IN.append(d_in)
    return IN, OUT
def dotmat(G):
    if(G.directed):
        c = " -> "
        s = "digraph {\n"
    else:
        c = " -- "
        s = "graph {\n"
    if(G.directed):
        for src in range(G.order):
            for dst in range(G.order):
                for n in range(G.adj[src][dst]):
                    s += str(src) + c + f"{dst}\n"
    else:
        for src in range(G.order):
            for dst in range(src,G.order):
                for n in range(G.adj[src][dst]):
                    s += str(src) + c + f"{dst}\n"
    return s + "}\n"
def dot(G):
    if(G.directed):
        c = " -> "
        s = "digraph {\n"
    else:
        c = " -- "
        s = "graph {\n"
    if(G.directed):
        for src in range(G.order):
            for dst in G.adjlists[src]:
                    s += str(src) + c + f"{dst}\n"
    else:
        for src in range(G.order):
            for dst in G.adjlists[src]:
                if(dst >= src):
                    s += str(src) + c + f"{dst}\n"
    return s + "}\n"
def BFS(G):
    M = [0] * G.order
    i = 0
    while sum(M) < G.order:
        while M[i] != 0:
            i+=1
        R = []
        Q = Queue()
        Q.enqueue(i)
        M[i] = 1
        R.append(i)
        while not Q.isempty():
            x = Q.dequeue();
            for y in range(G.order):
                if G.adj[x][y] and not M[y]:
                    Q.enqueue(y)
                    M[y] = 1
                    R.append(y)
        print(R)
def Vect(G):
    M = [0]*G.order
    R = [0]*G.order
    i = 0
    while sum(M) < G.order:
        while M[i] != 0:
            i+=1
        Q=Queue()
        Q.enqueue(i)
        R[i] = -1
        M[i] = 1
        while not Q.isempty():
            x = Q.dequeue()
            for y in G.adjlists[x]:
                if not M[y]:
                    Q.enqueue(y)
                    M[y] = 1
                    R[y] = x
    return R
def wrap(G): #both
    M = [0] * G.order
    for i in range(G.order):
        if not M[i]:
            #DFS0(G,i,M)
            DFS1(G,i,M)
            print()
def DFS0(G,x,M): #Gmat
    M[x] += 1
    print(x,end=" ")
    for y in range(G.order):
        if G.adj[x][y] and not M[y]:
            DFS0(G,y,M)
def DFS1(G,x,M): #G
    M[x] += 1
    print(x,end = " ")
    for y in G.adjlists[x]:
        if not M[y]:
            DFS1(G,y,M)
def DFS_parent(G):
    M = [0] * G.order
    P = [0] * G.order
    for i in range(G.order):
        if not M[i]:
            P[i] = -1
            DFSP0(G,i,M,P)
    return P
def DFSP0(G,x,M,P):
    M[x] += 1
    for y in G.adjlists[x]:
        if not M[y]:
            P[y] = x
            DFSP0(G,y,M,P)
def DFS3(G,x,p,M):
    M[x] += 1
    for y in G.adjlists[x]:
        if not M[y]:
            DFS3(G,y,x,M)
        elif y != p:
            print(x," -> ",y)
def wrap0(G):
    M = [0] * G.order
    for i in range(G.order):
        if not M[i]:
            DFS3(G,i,-1,M)
wrap0(G1)
