from lexar import Token 
from bnflexar import BnfLexar

class Grammar(object):
    """grammar is simply a list of rules with at least one start symbole"""
    def __init__(self ):
        self.rules=[]
        #self.startSymbole
        #we need to put the start symbole someware
    def generate(self, source, verbose=False):
        def __findbreaks( stack ,i, left):# we need to text this function 
            breaktok =Token(value="break") 
            newrule =Rule(left)
            if breaktok in stack[i:] :
                firstbreak = stack.index(breaktok,i)
                newrule.rightHand.extend(stack[i:firstbreak])
                self.rules.append(newrule)
                __findbreaks(stack, firstbreak+1,left)
            else:
                newrule.rightHand=stack[i:]
                self.rules.append(newrule)

        lex=BnfLexar()
        if verbose:
            lex.setVerbose()
        lex.scanFile(source)
        stream =lex.tokenStream
        pos = 0
        end = len(stream)
        while pos<end:
            stack = []
            delem = Token(value='end') 
            left=stream[pos]
            if delem in stream[pos:]:
                stop= stream.index(delem,pos)
                stack.extend(stream[pos:stop])
                left = stack[0]
                __findbreaks(stack,2,left)
            else:
                stack.extend(stream[pos:])
                left = stack[0]
                __findbreaks(stack,2,left)
                stop=len(stream)
            pos=stop+1

    def longMatch(self, lex1 ,lex2):
        if lex1 == None:
            return self.shortMatch(lex2)
        elif lex2 ==None:
            return self.shortMatch(lex1)
        else:
            for rule in self.rules:
                #print "long test",rule.rightHand, lex1, lex2
                if rule.rightHand == [lex1,lex2]:
                    print "return %s -> %s"%(rule.leftHand, lex1,lex2)
                    #print "return %s -> %s %s "%(rule.leftHand, lex1, lex2 )
                    return rule.leftHand
    def shortMatch(self, lex1):
         """ matches a list of terminals or nonterminal to a nonterminal"""
         for rule in self.rules:
            #print "short test",rule.rightHand, lex1
            if rule.rightHand == [lex1]:
                print "return %s -> %s"%(rule.leftHand, lex1)
                return rule.leftHand
    def __len__(self):
            return len(self.rules)
    def bnf2cnf(self):
        for rule in self.rules:
            self.__isolateTerminals(rule)
        for rule in self.rules:
            self.__binaryize(rule)
        self.rules=set(self.rules)
        self.rules = list(self.rules)

    def __isolateTerminals(self,rule): 
        #step 1 isolate termina0ls
        if len(rule.rightHand)>1: 
            for i in range(len(rule.rightHand)):
                token = rule.rightHand[i]
                if token.type=="terminal" :
                    left= Token("nonterminal", "U_%s"%token.value ) 
                    right=[Token("terminal",token.value)]
                    rule.rightHand[i]=Token("nonterminal","U_%s"%token.value)
                    self.rules.append(Rule(left,right) )

    def __binaryize(self,rule):        
        #step 2 make binary
        if len(rule.rightHand)> 2 :
            #make auxiliary rules 
            #we can do this recursively
            newToks=[]
            handLength=len(rule.rightHand)
            for i in rule.rightHand:
                newToks.append(Token("nonterminal","W_%s"%i.value) )
            oldRight=rule.rightHand
            rule.rightHand = [oldRight[0],newToks[0]]
            for i in range(1,handLength):
                self.rules.append(Rule(newToks[i-1],[ newToks[i], oldRight[i] ]) )#beautifull 
    def __removeEpsilon(self, rule):
        pass
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
    def __init__(self, nonterminal ,right=None):
        if right is None:
            right = []
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
            if token.type== "terminal":
                right+="' %s '"%token.value
            else:
                right+="< %s >"%token.value
        representation="{< %s > ::= %s }"%(self.leftHand.value,right)
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
   product="%s"%bnf.__str__()
   print "product \n %s"%product
   "test shortmatch"
   bnf.shortMatch(Token(value="("))


if __name__=='__main__':
    test()
