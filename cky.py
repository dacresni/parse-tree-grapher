from grammar import Grammar
from cyk import CYKChart
from telescope import Telescope
 
def solve():
    G = Grammar()
    source = open("cky.txt",'r')
    #source = open("metabnf",'r')
    G.generate(source)
    G.bnf2cnf()
    print "grammer==",G
    lexer= Telescope()
    balance=open('telescope','r')
#    balance=open('metabnf','r')
    lexer.scanFile(balance)
    S=lexer.getStream()
    print "stream ===",S
    C=CYKChart()
    C.Build_CYK_Chart(G,S)
 
if __name__=='__main__':
    solve()
