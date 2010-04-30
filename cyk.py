#! /usr/bin/env python
import sys
from lexar import Token
from grammar import Grammar
from bnflexar import BnfLexar

class CYKChart(object):
    def __init__(self):
        self.chart =[]
        #self.chart= [ [set() for _ in range(n)] for _ in range(n)]
    def Build_CYK_Chart (self, aGrammar,aString ) : # a 
        n = len(aString)+1
        self.chart= [ [set() for _ in range(n)] for _ in range(n)]
        print "in Build_CYK_Chart"
        print "aString",aString
        print "aGrammar",aGrammar
        for i in range(1,n):
            print "i=",i
            print "DEBUG: chart ",i,aString[i-1],aGrammar.singleMatch(aString[i-1]) 
            self.chart[i][1]=aGrammar.singleMatch(aString[i-1])
            print "After setting...",self.chart[i][1] 
        print "chart after len 1 dealt with\n",self
        for j in range(2,n): #range drops the endpoint
            for i in range(1,n-j+1):  # step 4 in pg 140 of Hopcroft and range is (first, last-1)
                for k in range(1,j-1):
                   print i,j,":=",i,k,",",self.chart[i][k],self.chart[i+k][j-k]
                   matches=aGrammar.setMatchLong(self.chart[i][k],self.chart[i+k][j-k])
                   self.chart[i][j].update(matches)
        #print self
                    #if nothings there, try the chart it MUST be in that order 
                #done
            #end for i
        #end for j
   #end def
    def __repr__(self):
        rep = ""
        for i in range(1,len(self.chart[0])):
           for j in range(1,len(self.chart[0])):
               rep+="%i,%i,%s"%(i,j,self.chart[i][j])
           rep+="\n"

    def __str__(self):
        rep = ""
        for i in range(1,len(self.chart[0])):
           for j in range(1,len(self.chart[0])):
               rep+="%i,%i,%s"%(i,j,self.chart[i][j])
           rep+="\n"
        return rep
