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
        n = len(aString)
 #       self.chart= [ [set() for _ in range(n)] for _ in range(n)]
        self.chart=Chart(len(aString))
        print "in Build_CYK_Chart"
        print "aString",aString
        print "aGrammar",aGrammar
        for i in range(1,n):
            print "i=",i
            print "DEBUG: chart i,0",aString[i],aGrammar.shortMatch(aString[i]) 
            self.chart.asign(i,1,aGrammar.shortMatch(aString[i]))
            print "After setting...",self.chart[i:0] 
        print "chart after len 1 dealt with\n",self
        for j in range(2,n): #range drops the endpoint
            for i in range(1,n-j+1):  # step 4 in pg 140 of Hopcroft and range is (first, last-1)
                for k in range(1,j-1):
                   print i-1,j-1,":=",i-1,k-1,",",self.chart[i:k],self.chart[i+k:j-k]
                   self.chart[i:j].update(aGrammar.setMatchLong(self.chart[i:k],self.chart[i+k:j-k]))
        #print self
                    #if nothings there, try the chart it MUST be in that order 
                #done
            #end for i
        #end for j
   #end def
    def __repr__(self):
        for i in range(len(self.chart[0])):
            for j in range(len(i)):
                for k in range(len(j)):
                    print k,j,i


    def __str__(self):
         rep = ""
         for i in range(len(self.chart)):
            for j in range(len(self.chart)):
                rep+="%i,%i,%s"%(j,i,self.chart[i:j])
            rep+="\n"
         return rep

class Chart(object):
    def __init__(self,n):
        self.chart= [ [set() for _ in range(n)] for _ in range(n)]
        self.demention=n
    def __len__(self):
        return self.demention
    def __getslice__(self,i,j):
        return self.chart[i-1][j-1]
    def asign(self,i,j,op):
        self.chart[i-1][j-1]=op
