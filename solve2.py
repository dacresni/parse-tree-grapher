from grammar import Grammar
from treecyk import CYKChart
from balance import BalanceLexer
from gra import genDot
def solve():
    from os import system
    G = Grammar()
    source = open("g1.txt",'r')
    #source = open("metabnf",'r')
    G.generate(source)
    G.bnf2cnf()
    print "grammer==",G
    lexer= BalanceLexer()
#    balance=open('easy.txt','r')
    balance=open('balance.txt','r')
    lexer.scanFile(balance)
    S=lexer.getStream()
    print "stream ===",S
    C=CYKChart()
    C.Build_CYK_Chart(G,S)
    print C
    print C.graph
    genDot(C,"testfile.dot")
    system("dot -Tjpg testfile.dot -o test2.jpg")
    print "test2.jpg created"

if __name__ == '__main__':
    solve()