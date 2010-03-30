#! /usr/bin/env python

"""
Let the input be a string S consisting of n characters: a1 ... an.
Let the grammar contain r nonterminal symbols R1 ... Rr.
This grammar contains the subset Rs which is the set of start symbols.
Let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
For each i = 1 to n
  For each unit production Rj -> ai, set P[i,1,j] = true.
For each i = 2 to n -- Length of span
  For each j = 1 to n-i+1 -- Start of span
      For each k = 1 to i-1 -- Partition of span
           For each production RA -> R'B RC
                   If P[j,k,B] and P[j+k,i-k,C] then set P[j,i,A] = true
                   If any of P[1,n,x] is true (x is iterated over the set s, where s are all the indices for Rs)
                        Then S is member of language
                        Else S is not member of language 

"""
import sys
from grammar import Token

def Build_CYK_Chart (aGrammar,aString) : # a 
    n = len(aString)
    chart = []# for n=5 thats [[][][][][]]
    for i in aString :
        chart.append([ aGrammar.shortMatch(i) ]) # append a list with the result of shortMatch(i) if no match, shortMatch should return None
    for j in  range(1,n+1): #range drops the endpoint
        for i in range(0,(n-j+1)+1):  # step 4 in pg 140 of Hopcroft and range is (first, last-1)
            chart[i].append([]) #append the empty set
            for k in range(0,j):
                chart[i][j] = chart[i][j] or aGrammar.longMatch(chart[i][k],chart[i+k][j-k]) #if nothings there, try the chart it MUST be in that orer 
            #done
        #end for i
    #end for j
#end def

def cyk(S,R):
    n= len(S) #needs to be a  list of leximmes returned by a scanner
    r=len(R)  #a grammar containing r nonterminals
    #X= the set of start symboles 
    P=[[true]*n]*n] # a 3 dimentional array
    for i in range(n):
        #production match
        for j in range(r):
            if (S[j] in R): #compare leximes with production rule
                P[i][0][j]= True
    for i in range(1,n): #Length of span aka the list of (formal)strings
        for j in range(n-i+1):
            for k in range(i-1):
               #For each production RA -> R'B RC
               #If P[j,k,B] and P[j+k,i-k,C] then set P[j,i,A] = true
                for p in filter(longMatch, R):
                    if (P[j][k][B] and P[j+k][i-k][C]): #we need to fix this line 
                     P[j][i][A] = True
    if (any(P[1][n][x])): #x is the start symbole subset of R, R-x
        return true
    else:
        return false

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


