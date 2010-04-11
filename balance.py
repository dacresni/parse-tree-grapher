from lexar import Scanner, Token
class BalanceLexer(Scanner):
    def leftPerens(self,match):
        result=match.string.strip("\n")    
        self.tokenStream.append(Token("terminal",result))
    def rightPerens(self,match):
        result=match.string.strip("\n")    
        self.tokenStream.append(Token("terminal",result))
    def __init__(self):
        specDict={
        r'\(':self.leftPerens,
        r'\)':self.rightPerens
        }
        Scanner.__init__(self,specDict)
    #we need to make it a policy to overwrite this functio
if __name__=='__main__':
# note, it won't import this grammar correctly
    readscann=BalanceLexer()
    readscann.setVerbose()
    print "end of verbose"
    try:
        meta = open('g1.txt','r')
    except IOError:
        print 'metabnf not found'
    readscann.scanFile(meta)
    print readscann.tokenStream
    print "BnfLexar imported sucessfully"
