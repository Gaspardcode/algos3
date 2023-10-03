from shutil import copyfile
copyfile('gaspard.torterat-slanda_prefixtrees.py','mycode.py') # creates copy

import mycode
import prefixtreesexample as ex

print("count words: ", mycode.countwords(ex.Tree1))
print("average length: ",mycode.averagelength(ex.Tree1))
print("word list: ", mycode.wordlist(ex.Tree1))
print("longest word: ", mycode.longestword(ex.Tree1))
print("search for 'castle': ", mycode.searchword(ex.Tree1,"castle"))
print("search for 'cat': ", mycode.searchword(ex.Tree1,"cat"))
print("Hangman")
for s in ("c__e", "_a__","____","ca__"):
    print('\t',s,"=>",mycode.hangman(ex.Tree1,s))

mycode.addword(ex.Tree1,"cat")
print("added cat")
print("3-letter words that begin with 'c': ",mycode.hangman(ex.Tree1,"c__")) 
print("word list: ", mycode.wordlist(ex.Tree1))
mycode.buildlexicon(ex.Tree1,"test.txt")
