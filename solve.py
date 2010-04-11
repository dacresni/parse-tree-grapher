from grammar import Grammar
from cyk import CYKChart
from balance import BalanceLexer
def solve():
    G = Grammar()
    source = open("g1.txt",'r')
    G.generate(source)
    G.bnf2cnf()
    lexer= BalanceLexer()
    balance=open('balance.txt','r')
    lexer.scanFile(balance)
    S=lexer.tokenStream
    C=CYKChart()
    C.Build_CYK_Chart(G,S)
    print C
if __name__ == '__main__':
    solve()
