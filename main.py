#! /usr/bin/env
from grammar import Grammar
from cyk import CYKChart
from viz import genVIZ 
from os import system
from os import sep
def main(args):
    lexarname =None
    gramarspec =None
    inputfile =None
    outputtype =None
    outputfile =None
    argc= len(args)
    if argc == 1: 
        print "usage: main.py  lexarname, gramarspec, inputfile,[output-type] [output-file ]\n"
        return
    if argc > 1 : 
        lexarname = args[1]
    if argc > 2 :
        gramarspec = args[2]
    if argc > 3 : 
        inputfile = args[3]
    if argc > 4 :
        outputtype=args[4]
    else:
        outputtype="dot"
    if argc > 5 :
        outputfile = args[5]
    else:
        outputfile = inputfile
    G = Grammar()
    source = open(gramarspec,'r')
    G.generate(source)
    G.bnf2cnf()
    print "grammer==",G
    if sep in lexarname:
        lexarname = lexarname.replace(sep,".")
    lexerclass=__import__(lexarname)
    lexer=lexerclass.Lexer()
    lexer.scan(inputfile)
    S=lexer.getStream()
    print "stream ===",S
    C=CYKChart()
    C.Build_CYK_Chart(G,S)
    print C
    print C.graph
    if outputtype=="dot":
        genDot(C,outputfile)
        system("dot -Tjpg %s  -o %s "%(outputfile, outputfile)) # todo, see if dot takes STDIN so I can pipe this to it 
        print "%s generated"%(outputfile)
    elif outputtype=="js":
       genVIZ(C,outputfile)

if __name__ == '__main__':
    import sys
    main(sys.argv)
    
