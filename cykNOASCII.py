#! /usr/bin/env python
import sys
from lexar import Token
from grammar import Grammar
class CYKChart(object):
    def __init__(self):
        self.chart = []
    def Build_CYK_Chart (self, aGrammar,aString, chart=self.chart) : # a 
        n = len(aString)
        chart = []# for n=5 thats [[][][][][]]
        for i in aString :
            chart.append([ aGrammar.shortMatch(i) ]) # append a list with the result of shortMatch(i) if no match, shortMatch should return None
        for j in  range(1,n+1): #range drops the endpoint
            for i in range(0,(n-j+1)+1):  # step 4 in pg 140 of Hopcroft and range is (first, last-1)
                chart[i].append([]) #append the empty set
                for k in range(0,j):
                    chart[i][j].append(chart[i][j] or aGrammar.shortMatch(chart[i][k],chart[i+k][j-k])) #if nothings there, try the chart it MUST be in that order 
                #done
            #end for i
        #end for j
    #end def
    def __repr__(self):
        return self.chart
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


