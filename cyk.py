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
        self.chart= [[""]*n]*n
        chart= self.chart
        print "aString",aString
        print "aGrammar",aGrammar
        for i in range(n):
            #print "chart i,0",chart[i][0],aString[i],aGrammar.shortMatch(aString[i]) 
            chart[i][0] = aGrammar.shortMatch(aString[i])  
        print "chart",chart
        for j in range(1,n): #range drops the endpoint
            for i in range(n-j+1):  # step 4 in pg 140 of Hopcroft and range is (first, last-1)
                #chart[i].append([]) #append the empty set
                for k in range(j):
                   #print "chart i,j ",chart[i][j],chart[i][k],chart[i+k][j-k], aGrammar.longMatch(chart[i][k],chart[i+k][j-k])
                   #print i,j
                   if chart[i][k] ==None or chart[i+k][j-k] == None :
                    pass
                   else:
                    chart[i][j]=aGrammar.longMatch(chart[i][k],chart[i+k][j-k])
                    #if nothings there, try the chart it MUST be in that order 
                #done
            #end for i
        #end for j
    #end def
    def __repr__(self):
        return self.chart

    def __str__(self):
        return "%s"%self.chart


