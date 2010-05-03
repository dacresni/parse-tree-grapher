#! /usr/bin/env python
import sys
from lexar import Token
from grammar import Grammar
from bnflexar import BnfLexar

class CYKChart(object):
    def __init__(self):
        self.chart =[]
        self.size=0
        self.string=""
        self.graph={}
        #self.chart= [ [set() for _ in range(n)] for _ in range(n)]
    def Build_CYK_Chart (self, aGrammar,aString ) : # a 
        n = len(aString)+1
        self.size=n
        self.string=aString
        self.chart= [ [set() for _ in range(n)] for _ in range(n)]
        #self.graph= [ [[] for _ in range(n)] for _ in range(n)] #lists are mutable
        print "in Build_CYK_Chart"
        print "aString",aString
        print "aGrammar",aGrammar
        print self
        for i in range(1,n):
            #print "i=",i
            #print "DEBUG: chart ",i,aString[i-1],aGrammar.singleMatch(aString[i-1]) 
            self.chart[i][1]=aGrammar.singleMatch(aString[i-1])
            #print "After setting...",self.chart[i][1] 
        print "chart after len 1 dealt with\n",self
        h='a'
        w='a'
        k='a'
        for w in range(2,n): #range drops the endpoint
            print h,w,k,"w"
            for h in range(1,n-w+1):  # step 4 in pg 140 of Hopcroft and range is (first, last-1)
                print h,w,k,"h"
                for k in range(1,w-1+1):
                   print h,w,k,"k"
                   print h,w,":=",
                   print "[%i,%i]%s"%(h,k,self.chart[h][w]),
                   print "[%i,%i]%s"%(h+k,w-k,self.chart[h+k][w-k])
                   set1=self.chart[h][k]
                   set2=self.chart[h+k][w-k]
                   #matches=aGrammar.setMatchLong(self.chart[h][k],self.chart[h+k][w-k])
                   matches=aGrammar.setMatchLong(set1,set2)
                   self.chart[h][w].update(matches)
                   #self.graph[h][w].append(CYKTree((h,w),(h,k),(h+k,w-k))) # coordinates of where i go and the lines
                   theKey=(h,w)
                   if len(matches )!=0:
                       self.graph.setdefault(theKey,[]).extend([(h,k),(h+k,w-k)])

        print self.graph
                    #if nothings there, try the chart it MUST be in that order 
                #done
            #end for i
        #end for j
   #end def
    def __len__(self):
        return self.size
    def __repr__(self):
        rep = ""
        for i in range(len(self.chart[0])):
           for j in range(len(self.chart[0])):
               rep+="%i,%i,%s"%(i,j,self.chart[i][j])
           rep+="\n"

    def __str__(self):
        rep = ""
        for i in range(1,len(self.chart[0])):
           for j in range(1,len(self.chart[0])):
               rep+="%i,%i,%s"%(i,j,self.chart[i][j])
           rep+="\n"
        return rep



def test(string='balance.txt', spec='g1.txt'):
    G = Grammar()
    source = open(spec,'r')
    #source = open("metabnf",'r')
    G.generate(source)
    G.bnf2cnf()
    print "grammer==",G
    lexer= BalanceLexer()
    balance=open(string,'r')
#    balance=open('metabnf','r')
    lexer.scanFile(balance)
    S=lexer.getStream()
    print "stream ===",S
    C=CYKChart()
    C.Build_CYK_Chart(G,S)
    print C

if __name__ == '__main__' :
    import sys
    if len(sys.argv)>1:
        test(sys.argv[1], sys.argv[2])
    else:
        print "usage: %s file specfile"%sys.argv[0]

