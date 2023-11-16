import sys
from importlib.machinery import SourceFileLoader
import time
myfile = "gaspard.torterat-slanda_prefixtrees.py"
mycode = SourceFileLoader('mycode',myfile).load_module()

if  __name__ == '__main__':
    if len(sys.argv) < 1:
        print("missing argument file")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        T = mycode.buildtree(file_path)
    except FileNotFoundError:
        print('No such file', file_path)
        sys.exit(1)

    start = time.perf_counter()
    print("count words: ", mycode.countwords(T))
    print("average length: ",mycode.averagelength(T))
    print("word list: ", len(mycode.wordlist(T)))
    print("longest word: ", mycode.longestword(T))
    print("search for 'castle': ", mycode.searchword(T,"castle"))
    print("search for 'cacahouete': ", mycode.searchword(T,"cacahouete"))
    print("Hangman")
    for s in ("c__e", "_y__","_","ca_"):
        print('\t',s,"=>",mycode.hangman(T,s))
    mycode.addword(T,"cat")
    mycode.addword(T,"catastrophe")
    mycode.addword(T,"dang")
    print("added cat")
    print("added catastrophe")
    print("added dang")
    print("3-letter words that begin with 'c': ",mycode.hangman(T,"c__")) 
#    print("word list: ", mycode.wordlist(ex.Tree1))
    end = time.perf_counter()
    print(f"Execution time : {end - start} sec")
