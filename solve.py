from grammar import Grammar
from cyk import CYKChart
from balance import BalanceLexer
def solve():
    G = Grammar()
    source = open("g1.txt",'r')
    #source = open("metabnf",'r')
    G.generate(source)
    G.bnf2cnf()
    print "grammer==",G
    lexer= BalanceLexer()
    balance=open('balance.txt','r')
#    balance=open('metabnf','r')
    lexer.scanFile(balance)
    S=lexer.getStream()
    print "stream ===",S
    C=CYKChart()
    C.Build_CYK_Chart(G,S)
    print C
if __name__ == '__main__':
    solve()
