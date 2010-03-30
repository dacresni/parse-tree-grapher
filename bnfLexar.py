from lexar import Token, Scanner 
# we can impliment the grammar parser inside the scanner lexer
# 3 out of 4 methods are going to be overloaded by the child  does the nested class inheret?
class Bnfparser(Scanner): #should I subclass this or not
    def rule(self,match):
        self.tokenStream.append(Token("rule",match.string) )
        print "the string %s matched the re %s"%(match.re,match.string)
    def equil(self,match):
        self.tokenStream.append(Token("equils") )
    def literal(self,match):
        self.tokenStream.append(Token("terminal",match.string))
        print "the string %s matched the re %s"%(match.re,match.string)
    def brake(self,match):
        self.tokenStream.append(Token("break"))
        print "break matched"
    def __init__(self):
        specDict={
            '<?P<rule>>': self.rule,
            '"?P<literal>"':self.literal,
            '\|':self.brake,
            '::=':self.equil
        }
        self.tokenStream=[]
        Scanner.__init__(self,specDict) #how you initialize parent class
if __name__=='__main__' :
    instance = Bnfparser() #don't forget the end perentheces
# note, it won't import this grammar correctly
    string = """
<syntax> ::= <rule> | <rule> <syntax>
 <rule>   ::= <opt-whitespace> "<" <rule-name> ">" <opt-whitespace> "::=" 
                 <opt-whitespace> <expression> <line-end>
 <opt-whitespace> ::= " " <opt-whitespace> | ""  
 <expression>     ::= <list> | <list> "|" <expression>
 <line-end>       ::= <opt-whitespace> <EOL> | <line-end> <line-end>
 <list>    ::= <term> | <term> <opt-whitespace> <list>
 <term>    ::= <literal> | "<" <rule-name> ">"
 <literal> ::= '"' <text> '"' | "'" <text> "'"  """
    #def scanString(self, string):
    print string
    instance.setVerbose()
    instance.scanString(string)
    for token in instance.tokenStream:
        print token
    print instance
    print "Bnfparser imported sucessfully"


