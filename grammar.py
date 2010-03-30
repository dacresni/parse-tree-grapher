from lexar import Token 
from bnflexar import BnfLexar

class Grammar(object):
    """ a grammar is simply a list of rules with at least one start symbole"""
    def __init__(self ):
        self.rules=[ ]
        self.ruleDict = {}
        #self.startSymbole
        #we need to put the start symbole someware
    def __repr__(self):
        for i in rules:
            print i
    def generate(self, source, verbose=False):
        lex=BnfLexar()
        if verbose:
            lex.setVerbose()
        #source=open('metabnf','r')
        lex.scanFile(source)
        newGrammer = Grammar()
        stream =lex.tokenStream
        #just for testing
        print stream
        pos = 0
        end = len(stream)
        def findbreaks(stack ,i, left):
            firstbreak = stack[i:].index(Token("break"))
            newrule =Rule(left)
            newrule.rightHand.extend(stack[i+1:firstbreak])
            newGrammer.rules.append(newrule)
            return findbreaks(stack, firstbreak,left)

        while stream[pos]!= end:
            stack = []
            #genrule
            while stream[pos].type != "equils":
                stack.append(stream[pos])
                pos+=1
            #here stream[pos] is ::=
            print stack
            left=stack[0]
            if(Token("break") in stack):
                pos = findbreaks(stack,0,left)
            else:
                newrule=Rule(left)
                newrule.rightHand.extend(stack[2:])# ::= is at stack[1]
                pos +=len(stack)
            pos-=1
            #another function 
    def shortMatch(self, lex1 ,lex2=""):
        """ matches a list of terminals or nonterminal to a nonterminal"""
        rightHand=(lex1,lex2) #make a tuple
        if  self.ruleDict[rightHand]:
            return leftHand
    def __len__(self):
            return len(self.rules)
    def bnf2cnf(self):
        for rule in self.rules:
            __isolateTerminals(rule)
        for rule in self.rules:
            __binaryize(rule)

    def __isolateTerminals(self,rule): 
        #step 1 isolate termina0ls
        for i in range(len(rule.rightHand)):
            token=rule.rightHand[i]
            if token.value!=None: 
                newrule=Rule( Token("terminal_%s"%token.value ),Token("terminal","%s"%token.value)  )
                self.rules.append(newrule)
                newrule.rightHand.insert(i,Token("terminal_%s"%token.value))

    def __binaryize(self,rule):        
        #step 2 make binary
        if len(rule.rightHand)> 2 :
            #make auxiliary rules 
            #we can do this recursively
            newToks=[]
            handLength=len(rule.rightHand)
            for i in rule.rightHand:
                newToks.append(Token("aux_%s"%i.value) )
            oldRight=rule.rightHand
            rule.rightHand = [oldRight[0],newToks[0]]
            for i in range(1,handLength):
                self.rules.append(Rule(newToks[i-1],[ newToks[i], oldRight[i] ]) )#beautifull 
    def __uniProductionsEleminate(self, rule):
        """eleminate unit productions """
        pass
    def __str__(self):
        representation = ""
        for rule in self.rules:
            representation+="%s\n"%(rule)
class Rule(object):
    # a rule in a grammar has a left hand side of 1 token and a right hand side of a
    def __init__(self, nonterminal ,right=[]):
        self.leftHand=nonterminal # a nonterminal token probibly
        self.rightHand=right 
        #perhaps we could shove these into a dict
    def __str__(self):
        right = ""
        for token in self.rightHand:
            right+="%s"%token
        representation="{%s ::=%s }"%(self.leftHand,right)
        return representation

if __name__=='__main__':
   try:
    source=open('metabnf','r')
   except IOError:
    print "metabnf not found"
   bnf=Grammar()
   bnf.generate(source,True)
   print bnf
