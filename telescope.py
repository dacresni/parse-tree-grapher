from lexar import Scanner, Token
class Telescope(Scanner):
    def __init__(self):
        specDict={
        r'(I|man|telescope|with|saw|cat|dog|pig|hill|park|roof|from|on|in)':self.terminal
        }
        Scanner.__init__(self,specDict)
    def terminal(self,match):
        self.tokenStream.append(Token("terminal",match.string))

if __name__=='__main__':
    scann=Telescope()
    scann.setVerbose()
    myfile=open("telescope",'r')
    scann.scanFile(myfile)
    print scann
    print scann.tokenStream
