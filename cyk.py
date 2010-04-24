#! /usr/bin/env python
import sys
from lexar import Token
from grammar import Grammar
from bnflexar import BnfLexar

class CYKChart(object):
    def __init__(self):
        self.chart =[]
    def Build_CYK_Chart (self, aGrammar,aString, ) : # a 
        n = len(aString)
        self.chart= [ [None]*n for _ in range(n)]
        print "in Build_CYK_Chart"
        print "aString",aString
        print "aGrammar",aGrammar
        for i in range(n):
            print "i=",i
            print "DEBUG: chart i,0",aString[i],aGrammar.shortMatch(aString[i]) 
            self.chart[i][0] = aGrammar.shortMatch(aString[i])  
            print "After setting...",self.chart[i][0]
        print "chart after len 1 dealt with",self
        for j in range(n): #range drops the endpoint
            for i in range(n-j+1):  # step 4 in pg 140 of Hopcroft and range is (first, last-1)
                for k in range(j-1):
                   print i,j,":=",i,k,",",i+k,j-k
                   self.chart[i][j]=aGrammar.longMatch(self.chart[i][k],self.chart[i+k][j-k])
                    #if nothings there, try the chart it MUST be in that order 
                #done
            #end for i
        #end for j
    #end def
    def __repr__(self):
        return self.chart

    def __str__(self):
        # j as outer loop
        # i as inner loop, up to n-j+1?
        return "%s"%self.chart


