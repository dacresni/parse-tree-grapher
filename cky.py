from grammar import Grammar
from treecyk import CYKChart
from telescope import Telescope
from graphviz import genDot
def solve():
    G = Grammar()
    source = open("cky.txt",'r')
    G.generate(source)
    G.bnf2cnf()
    print "grammer==",G
    lexer= Telescope()
    balance=open('telescope','r')
    lexer.scanFile(balance)
    S=lexer.getStream()
    print "stream ===",S
    C=CYKChart()
    C.Build_CYK_Chart(G,S)
    genDot(C)
 
if __name__=='__main__':
    solve()
