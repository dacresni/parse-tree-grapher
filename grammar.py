from lexar import Token 
from bnflexar import BnfLexar

class Grammar(object):
    """grammar is simply a list of rules with at least one start symbole"""
    def __init__(self ):
        self.rules=[ ]
        #self.startSymbole
        #we need to put the start symbole someware
    def generate(self, source, verbose=False):
        def __findbreaks( stack ,i, left):# we need to text this function 
            breaktok =Token("break") #### ############# there should be no  break tokens in this grammar
            newrule =Rule(left)
            if breaktok in stack[i:] :
                firstbreak = stack.index(breaktok,i)
		print "breakFound %s"%firstbreak
                print firstbreak
                newrule.rightHand.extend(stack[i:firstbreak])
                self.rules.append(newrule)
                __findbreaks(stack, firstbreak+1,left)
                #wehre
            else:
                newrule.rightHand.extend(stack[i:])
                self.rules.append(newrule)
        
        def __findEq(self, stack):
            equiltok = Token("equils")
            if not equiltok in stack:
                print "something's up"
            else:
                left = stack[0]
                __findbreaks(stack,2,left)
        
        lex=BnfLexar()
        if verbose:
            lex.setVerbose()
        lex.scanFile(source)
        stream =lex.tokenStream
	print "stream==%s"%stream
        pos = 0
        end = len(stream)
       #just for testing
       # print "stream"%stream
        
        while pos<end:
            stack = []
            delem = Token('end') 
            left=stream[pos]
            print 'delem',delem
            print 'left',left
            print 'pos',pos
            if delem in stream[pos:]:
                stop= stream.index(delem,pos)
                print 'stop',stop
                stack.extend(stream[pos:stop])
                __findEq(stack)
            else:
                newRul=Rule(stack[0])
                newRul.rightHand.extend(stack[2:])
                self.rules.append(newRul)
            stop=len(stream)
            stack.extend(stream[pos:stop])
            print "stack",stack
            pos=stop+1

    def shortMatch(self, lex1 ,lex2=""):
        """ matches a list of terminals or nonterminal to a nonterminal"""
        for rule in self.rules:
            if rule.rightHand == [lex1 ,lex2]:
                return rule.leftHand
            else:
                return None
    def __len__(self):
            return len(self.rules)
    def bnf2cnf(self):
        for rule in self.rules:
            self.__isolateTerminals(rule)
        for rule in self.rules:
            self.__binaryize(rule)

    def __isolateTerminals(self,rule): 
        #step 1 isolate termina0ls
        if len(rule.rightHand)>1: 
            for i in range(len(rule.rightHand)):
                token = rule.rightHand[i]
                if token.type=="terminal" :
                    left= Token( type ="terminal_%s"%token.value ) 
                    right=[Token("terminal","%s"%token.value)]
                    rule.rightHand[i]=Token(type="terminal_%s"%token.value)
                    self.rules.append(Rule(left,right) )

    def __binaryize(self,rule):        
        #step 2 make binary
        if len(rule.rightHand)> 2 :
            #make auxiliary rules 
            #we can do this recursively
            newToks=[]
            handLength=len(rule.rightHand)
            for i in rule.rightHand:
                newToks.append(Token(type="aux_%s"%i.value) )
            oldRight=rule.rightHand
            rule.rightHand = [oldRight[0],newToks[0]]
            for i in range(1,handLength):
                self.rules.append(Rule(newToks[i-1],[ newToks[i], oldRight[i] ]) )#beautifull 
    def __uniProductionsEleminate(self, rule):
        """eleminate unit productions """
        pass
    def __str__(self):
        rep=[]
        for i in self.rules:
            rep.append("%s"%i)
        return "%s"%rep
    def __repr__(self):
        rep=[]
        for i in self.rules:
            rep.append("%s"%i)
        return "%s"%rep
        
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
        representation="{ %s ::=%s }"%(self.leftHand,right)
        return representation
    def __repr__(self):
        right = ""
        for token in self.rightHand:
            right+="%s"%token
        representation="{ %s ::=%s }"%(self.leftHand,right)
        return representation

def test():
   try:
    source=open('g1.txt','r')
   except IOError:
    print "metabnf not found"
   bnf=Grammar()
   
   bnf.generate(source,True)
   print "oldgrammar" 
   print bnf
   bnf.bnf2cnf()
   print "new grammer"
   print bnf
   product="%s"%bnf.__str__()
   print "product \n %s"%product
if __name__=='__main__':
    test()
