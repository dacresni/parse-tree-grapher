from lexer import Scanner, Token
class BalanceLexer(Scanner):
    def leftPerens(self,match):
        self.tokenStream.append(Token("terminal",match.string))
    def rightPerens(self,match):
        self.tokenStream.append(Token("terminal",match.string))
    def __init__(self):
        specDict={
        r'(':self.leftPerens,
        r')':self.rightPerens
        }
        Scanner.__init__(self,specDict)
    #def scan(self, filename)
    #we need to make it a policy to overwrite this functio
        

