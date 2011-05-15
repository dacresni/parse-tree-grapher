from grammar import Grammar
from cyk import CYKChart
from infixlex import Infix
from viz import genDot
def solve():
    from os import system
    G = Grammar()
    source = open("infix.txt",'r')
    G.generate(source)
    G.bnf2cnf()
    print "grammer==",G
    lexer= Infix()
    balance=open('input.txt','r')
    lexer.scanFile(balance)
    S=lexer.getStream()
    print "stream ===",S
    C=CYKChart()
    C.Build_CYK_Chart(G,S)
    print C
    print C.graph
    genDot(C,"infix.dot")
    system("dot -Tjpg infix.dot -o infix.jpg")
    print "infix.jpg created"

if __name__ == '__main__':
    solve()
