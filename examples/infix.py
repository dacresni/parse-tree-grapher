from lexar import Scanner, Token
class Infix(Scanner):
    def __init__(self):
        specDict={
        r'x':self.terminal,
        r'y':self.terminal,
        r'z':self.terminal,
        r'\+':self.terminal,
        r'\*':self.terminal,
        r'\-':self.terminal,
        r'/':self.terminal,
        r'\)':self.terminal,
        r'\(':self.terminal
        }
        Scanner.__init__(self,specDict)
    def terminal(self,match):
        result=match.string.strip("\n")    

