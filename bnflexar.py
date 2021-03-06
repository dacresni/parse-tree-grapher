from lexar import Token, Scanner 
# we can impliment the grammar parser inside the scanner lexer
# 3 out of 4 methods are going to be overloaded by the child  does the nested class inheret?
class Lexer(Scanner): #should I subclass this or not
    def rule(self,match):
        result=match.string.strip('\n',)    
        self.tokenStream.append(Token("nonterminal",result) )
    def equil(self,match):
        self.tokenStream.append(Token(value="equils") )
    def literal(self,match):
        result=match.string.strip('\n"')    
        self.tokenStream.append(Token("terminal",result))
    def brake(self,match):
        self.tokenStream.append(Token(value="break"))
    def end(self,match):
        self.tokenStream.append(Token(value="end"))
    def epsilon(self,match):
        self.tokenStream.append(Token(value="epsilon"))
       
    def __init__(self):
        specDict={
           r'^".+"$':self.literal,
           r'^\<\S+\>$': self.rule, 
           r'\|':self.brake,
           r'::=':self.equil,
           r';':self.end,
           r'""':self.epsilon,
        }
        Scanner.__init__(self,specDict) #how you initialize parent class
if __name__=='__main__' :
    from bnflexar import BnfLexar
    instance =BnfLexar() #don't forget the end perentheces
# note, it won't import this grammar correctly
    print string
    instance.setVerbose()
    print "end of verbose"
    try:
        meta = open('g1.txt','r')
        instance.scanFile('g1.txt')
    except IOError:
        print 'file not found'
    print instance.tokenStream
    print "BnfLexar imported sucessfully"
