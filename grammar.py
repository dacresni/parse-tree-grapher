from lexar import Token 
from bnflexar import BnfLexar

class Grammar(object):
    """grammar is simply a list of rules with at least one start symbole"""
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
        lex.scanFile(source)
        newGrammer = Grammar()
        stream =lex.tokenStream
        pos = 0
        end = len(stream)
       #just for testing
        print stream
        def findbreaks(stack ,i, left):# we need to text this function 
            breaktok =Token("break") 
                firstbreak = stack[i:].index(breaktok)
            newrule =Rule(left)
            newrule.rightHand.extend(stack[i+1:firstbreak])
            newGrammer.rules.append(newrule)
            findbreaks(stack, firstbreak,left)
        #base case 
        while pos!= end:
            stack = []
            #here stream[pos+1] is ::=
            #genrule
            left=stream[pos] #this should be a left hand rule
            stop =stream.index( Token("equils"),pos+1) # the last 'equils' after the rule 
            #which should be the start of the next rule 
            stack.extend(stream[pos+1:stop])# this time i ommetted the ::= 
            print stack
            breaktok=Token("break") 
            if(breaktok in stack):
                newrule=Rule(left)
                newrule.rightHand.extend(stack)# ::= is at stack[1]
            else:
                findbreaks(stack,0,left) #we should prove the base case before we do this 
            pos=stop-1
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
    """ a rule in a grammar has a left hand side of 1 token and a right hand side of a """
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

def test():
   try:
    source=open('g1.txt','r')
   except IOError:
    print "metabnf not found"
   bnf=Grammar()
   bnf.generate(source,True)
   print bnf
if __name__=='__main__':
    test()
