from lexar import Token 
from bnflexar import Lexer

class Grammar(object):
    """grammar is simply a list of rules with at least one start symbole"""
    def __init__(self ):
        self.rules=[]
        #self.rules = set(self.rules  )
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

        lex=Lexer()
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
    def singleMatch(self, lex):
        """ matches a list of terminals or nonterminal to a nonterminal"""
        matches = set()
        for rule in self.rules:
           #print "short test",rule.rightHand,lex
           if rule.rightHand == [lex]:
               #print "return %s -> %s"%(rule.leftHand, lex)
               matches.add(rule.leftHand)
        return matches 

    def longMatch(self, lex1 ,lex2):
        matches = set()
        for rule in self.rules:
            #print "long test",rule.rightHand, lex1, lex2
            if rule.rightHand == [lex1,lex2]:
                #print "return %s -> %s %s"%(rule.leftHand, lex1,lex2)
                matches.add(rule.leftHand)
        return matches 
    def shortMatch(self, set1):
        matches=set()
        for rule in self.rules:
           #print "short test",rule.rightHand, set1
           if rule.rightHand == [set1]:
               print "return %s -> %s"%(rule.leftHand, set1)
               matches.add(rule.leftHand)
        return matches

    def setMatchShort(self,set1):
        matches=set()
        if len(set1)!=0:
            for lex in set1:
                matches.update(self.shortMatch(lex))
        return matches
    def setMatchLong(self, set1, set2):
        matches=set()
        for item1 in set1:
            for item2 in set2:
                matches.update(self.longMatch(item1,item2))# ordanance does matter
        return matches
    def __len__(self):
            return len(self.rules)
    def bnf2cnf(self):
        for rule in self.rules:
            self.__isolateTerminals(rule)
        print self
        for i in range(len(self.rules)) :
            self.__binaryize(self.rules[i],i )
        print self
        self.rules=set(self.rules)

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


    def __binaryize(self,rule,index):        
        #step 2 make binary
        if len(rule.rightHand)> 2 :
            #make auxiliary rules 
            newToks=[]
            hand=len(rule.rightHand)
            for i in range(1,hand-1):
                newToks.append(Token("nonterminal","aux%i-%i"%(index,i) ))
            newToks.append(rule.rightHand[-1] )
            oldRight=rule.rightHand
            rule.rightHand = [oldRight[0],newToks[0]]
            for i in range(1,hand-1):
                self.rules.append(Rule(newToks[i-1],[oldRight[i],newToks[i]]))



    def __removeEpsilon(self, rule):
        pass
    def __uniProductionsEleminate(self, rule):
        """eleminate unit productions """
        pass
    def __str__(self):
        rep=""
        for i in self.rules:
            rep+=(" %s "%i)
        return rep
    def __repr__(self):
        rep=""
        for i in self.rules:
            rep.append("{%s}\n"%i)
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
            right+=" %s "%token.value
        representation=" %s ::= %s "%(self.leftHand.value,right)
        return representation
    def __hash__(self):
        return hash("%s"%self)
    def __eq__(self, other ):
        return (self.leftHand == other.leftHand and self.rightHand ==other.rightHand)
        
 
def test(filename=None):
   source = None
   if filename==None:
    filename="examples/balance.txt"
   try:
    source=open(filename,'r')
    bnf=Grammar()
    bnf.generate(source,True)
    print "oldgrammar",
    print bnf
    bnf.bnf2cnf()
    print "product"
    print bnf
   except IOError:
    print "metabnf not found"
    raise IOError(filename)

if __name__=='__main__':
    import sys
    if len(sys.argv)>1:
        print "calling with",sys.argv[1]
        test(sys.argv[1])
    else:
        test()
