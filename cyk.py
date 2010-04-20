#! /usr/bin/env python
import sys
from lexar import Token
from grammar import Grammar
from bnflexar import BnfLexar

class CYKChart(object):
    def __init__(self):
        self.chart = []
    def Build_CYK_Chart (self, aGrammar,aString, ) : # a 
        n = len(aString)
        chart = [[None]*n]*n
        self.chart=chart
        print chart
        print "aString",aString
        print "aGrammar",aGrammar
        for i in range(n):
            chart[i][0]= aGrammar.shortMatch(aString[i])  # append a list with the result of shortMatch(i) if no match, shortMatch should return None
        print "chart",chart
        for j in range(1,n): #range drops the endpoint
            for i in range(n-j+1):  # step 4 in pg 140 of Hopcroft and range is (first, last-1)
                print i,j
                #chart[i]=None #append the empty set
                for k in range(j):
                    if chart[i][j]==None:
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


