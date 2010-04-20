#! /usr/bin/env python
import sys
from lexar import Token
from grammar import Grammar

class CYKChart(object):
    def __init__(self):
        self.chart =[]
    def Build_CYK_Chart (self, aGrammar,aString, ) : # a 
        n = len(aString)
        self.chart= [[None]*n]*n
        chart= self.chart
        print "aString",aString
        print "aGrammar",aGrammar
        for i in range(n):
            chart[i][0]= aGrammar.shortMatch(aString[i])  # append a list with the result of shortMatch(i) if no match, shortMatch should return None
        print "chart",chart
        for j in range(1,n): #range drops the endpoint
            for i in range(n-j+1):  # step 4 in pg 140 of Hopcroft and range is (first, last-1)
                print i,j
                #chart[i].append([]) #append the empty set
                for k in range(j):
                    if chart[i][j] == None:
                        chart[i][j]=aGrammar.longMatch(chart[i][k],chart[i+k][j-k])
                    #if nothings there, try the chart it MUST be in that order 
                #done
            #end for i
        #end for j
    #end def
"""
Let Close(X) = { B | B →* A, using unary productions, and A ϵ X}
Build CYK Chart(t,[w1 ,. . . ,wn ])
    for j ← 1 to n do
        t(j-1, j) ← Close({ wj })
    for k ← 1 to n
        for j ← k to n
            for m ← 1 to k-1 do
                t(j-k, j) ← t(j-k, j) ∪ Close({ A | A → B C
                    for some B ∈ t(j-k, j-m) and C ∈ t(j-m, j)})
"""


