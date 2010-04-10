from lexar import Token, Scanner 
# we can impliment the grammar parser inside the scanner lexer
# 3 out of 4 methods are going to be overloaded by the child  does the nested class inheret?
class BnfLexar(Scanner): #should I subclass this or not
    def rule(self,match):
        self.tokenStream.append(Token("rule",match.string) )
    def equil(self,match):
        self.tokenStream.append(Token("equils") )
    def literal(self,match):
        self.tokenStream.append(Token("terminal",match.string))
    def brake(self,match):
        self.tokenStream.append(Token("break"))
    def __init__(self):
        specDict={
            r'^".+"$':self.literal,
           r'^\<\S+\>$': self.rule, 
            r'\|':self.brake,
            r'::=':self.equil
        }
        Scanner.__init__(self,specDict) #how you initialize parent class
if __name__=='__main__' :
    instance = BnfLexar() #don't forget the end perentheces
# note, it won't import this grammar correctly
    print string
    readscann=BnfLexar()
    readscann.setVerbose()
    print "end of verbose"
    try:
        meta = open('g1.txt','r')
    except IOError:
        print 'metabnf not found'
    readscann.scanFile(meta)
    for token in readscann.tokenStream:
        print token
    print "BnfLexar imported sucessfully"