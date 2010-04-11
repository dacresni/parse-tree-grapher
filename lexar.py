""" a python lexer and lexer generator to return a scanner and produce lexers for the cyk algorithm to parse """

import re
class Token(object):
    def __init__(self,type, value=None):
        if value == None:
            self.type="terminal"
            self.value=type
        else:
            self.type=type
            self.value=value
    def __len__(self):
        return len(self.tokenStream)
    def __str__(self):
        return "(%s,%s)"%(self.type, self.value) #yes, None prints None
    def __repr__(self):
        return "(%s,%s)"%(self.type, self.value) #yes, None prints None
    def __eq__(self, other):
        return (self.type == other.type and self.value == other.value)
class Scanner(object):
    """ takes a dictionary of regex:function object pairs
        functions should expect match objects as parameters 
    """
    def __init__(self,spec):
        self.verbose=False
        self.patterns=[]
        self.actions=[]
        self.tokenStream = []
#we'll turn this into paralell lists.
        #this could be done with map()
        for k in spec.iterkeys():
            self.patterns.append(re.compile(k))
            self.actions.append(spec[k])
    def __getitem__(self,other):
        for i in range(len(self.patterns)):
        #for i in self.patterns:
            match =self.patterns[i].match(other) #returns a match object
            if (match):
                self.actions[i](match)
                if self.verbose:
                    print "matched %s with %s"%(match.string,self.patterns[i].pattern )
                    #we could turn this into a decorator later
                #actions should be callable (impliment __call__()
                #and expect a match object as a parameter
    def scanChar(self, string):
        """scans a string"""
        for word in string:
               self[word]
               #does do subword matches
    def scanFile(self, file):
        """ takes a flle and processes that file according to the spec"""
        for line in file:
            for word in line.split(' '):
               self[word]
               #doesnt do sub word matches 
    def scanWord(self,string):
        """ scans a string split by white space"""
        for word in string.split(' '):
            self[word]
        #we should make a more malualbe 


    def setVerbose(self):
        """sets behavior to print out the pattern matched at every match""" 
        self.verbose = True
    def unsetVerbose(self):     
        self.verbose = False
    def __str__(self):
        representation= '{'
        for i in range (len(self.patterns)):
            representation+=" %s : %s ,"%(self.patterns[i].pattern ,self.actions[i].__name__)
        representation+= '}'
        return representation
        #print each rule action pair

if __name__=='__main__' :
	from balance import BalanceLexer
	lex=BalanceLexer()
	lex.setVerbose()
	source =open('g1.txt')
	lex.scanFile(source)
	stream =lex.tokenStream
	print "stream==%s"%stream
	token = Token("token")
	print "token created sucessfully"
