__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixtrees.py 2023-10-03'

"""
Prefix Trees homework
2023-10 - S3
@author: gaspard.torterat-slanda 
"""

from algo_py import ptree

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

##############################################################################
## Measure

def countwords(T):
    """ count words in the prefix tree T (ptree.Tree)
    return type: int
    """
    
    if T.key[1]:
        return 1 + sum(countwords(child) for child in T.children)
    else:
        return sum(countwords(child) for child in T.children)

def averagelength(T):
    """ average word length in the prefix tree T (ptree.Tree)
    return type: float
    """
    nb_words, sum_lengths = __al(T,0)
    return sum_lengths/nb_words
    
def __al(T, h):
    """ sums heights and counts words in the prefix tree T
    return type: (int,int) 
    """
    nb, su = 0,0
    if T.key[1]:
        nb += 1
        su += h
    for child in T.children:
        temp_nb, temp_su = __al(child,h+1);
        nb += temp_nb
        su += temp_su
    return nb, su

###############################################################################
## Search and list

def wordlist(T):
    """ generate the word list, in alphabetic order, of the prefix tree T (ptree.Tree)
    return type: str list
    """
    return __wl(T,"") 

def __wl(T,w):
    """ returns the word list, in alphabetic order, of the prefix tree T
    param type w: str
    return type: str list
    """
    W = []
    w += T.key[0]
    if T.key[1]:
        W += [w]
    for child in T.children:
        W += __wl(child,w)
    return W

def longestword(T):
    """ search for the longest word in the prefix tree T (ptree.Tree)
    return type: str    
    """
    W = wordlist(T)
    max_ = 0
    word = "" 
    n = len(W)
    for i in range(0,n):
        if len(W[i]) > max_:
            word = W[i]
            max_ = len(W[i])
    return word 


def searchword(T, w):
    """ search for the word w (str) not empty in the prefix tree T (ptree.Tree)
    return type: bool
    """
    if w == "":
        return T.key[1]
    else:
        for child in T.children:
            if(child.key[0] == w[0]):
                return searchword(child,w[1:])
        return False
    

def hangman(T, pattern):
    """ Find all solutions for a Hangman puzzle in the prefix tree T: 
        words that match the pattern (str not empty) where letters to fill are replaced by '_'
    return type: str list
    """
    W = wordlist(T)
    n = len(pattern)
    P = [l for l in range(0,n) if(pattern[l]) != '_']
    n1 = len(P)
    H = []
    for word in W:
        if len(word) == n:
            i = 0
            while i < n1 and word[P[i]] == pattern[P[i]]:
                i += 1
            if i == n1:
                H += [word]
    return H

                
###############################################################################
## Build

def buildlexicon(T, filename):
    """ save the tree T (ptree.Tree) in the new file filename (str)
    """
    
    f = open(filename, "w")
    W = wordlist(T)
    for word in W:
        f.write(f"{word}\n")
    f.close()

def addword(T, w):
    """ add the word w (str) not empty in the tree T (ptree.Tree)
    """
    if w == "":
        T.key = (T.key[0], True)
        return None
    else:
        call = 1
        for child in T.children:
            if child.key[0] == w[0]:
                call = addword(child, w[1:])
        if call != None:
            i = 0
            n = T.nbchildren
#            print("BEFORE: ",end = "")
#            print("[",end = "")
#            for child in T.children:
#                print(child.key[0], end = ' ')
#          print("]\nAFTER: ",end = "")

            while i < n and T.children[i].key[0] < w[0]:
                i+=1
            T.children += [None]##
            for j in range(n,i,-1):#T.children.insert(i-1,ptree.Tree((w[0],False)))
                T.children[j] = T.children[j-1]
            T.children[i] = ptree.Tree((w[0],False))##
 #           print("[",end = "")
 #           for child in T.children:
 #               print(child.key[0], end = ' ')
 #           print("]")
            return addword(T.children[i],w[1:])
        else:
            return None


def buildtree(filename):
    """ build the prefix tree from the lexicon in the file filename (str)
    return type: ptree.Tree
    """
    f = open(filename,'r')
    T = ptree.Tree(("",False))
    for l in f:
        addword(T,l[:-1])
    f.close()
    return T
