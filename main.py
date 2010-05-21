from grammar import Grammar
from cyk import CYKChart
from viz import genDot
from os import system
def main(lexarname, gramarspec, inputfile, outputfile=None):
    if outputfile == None:
        outputfile = inputfile
    G = Grammar()
    source = open(gramarspec,'r')
    G.generate(source)
    G.bnf2cnf()
    print "grammer==",G
    lexer=__import__(lexarname)
    lexer.scan(inputfile)
    S=lexer.getStream()
    print "stream ===",S
    C=CYKChart()
    C.Build_CYK_Chart(G,S)
    print C
    print C.graph
    genDot(C,outputfile)
    system("dot -Tjpg %s  -o %s  "%(outputfile, outputfile))
    print "%s ted"%(outputfile)

if __name__ == '__main__':
    import sys
    main(sys.argv)
