from treecyk import CYKChart
class genDot(object):
    def genTree(self,G,here,visited):
        neighbors=G
        if not here in visited:
            visited.add(here)
            if neighbors.has_key(here):  # if it has neighbors
                for next in neighbors[here]:
                    self.edges.add((here,next))
                    self.genTree(G,next,visited)
    #if your not connected, you wont be in the bfs        
    def __init__(self,C,filename=None):
        if filename==None:
            self.filename="testfile.dot"
        else:
            self.filename=filename
        self.specFile=""
        self.edges=set()
        self.visited = set()
        print C.graph
        if not C.graph.has_key((1,len(C)-1)):
            raise Exception("parse error")
        self.genTree(C.graph, (1,len(C)-1),self.visited )
        for edge in self.edges:
            to = edge[0]
            fro = edge[1]
            self.specFile+='  "%s" -> "%s" ;\n'%(to,fro )
            #self.specFile+='  "%s" -> "%s" ;\n'%( "(%s,%s)"%(to[0],to[1]), "(%s,%s)"%(fro[0],fro[1]) )
        for node in self.visited :
            lable=C.chart[node[0]][node[1]]
            self.specFile+='    "%s"[label = "%s"] ;\n'%(node,lable ) #find lable for leaf node 

        finalFile=open(self.filename,'w')
        finalFile.write("digraph G { \n")
        finalFile.write(self.specFile)
        finalFile.write("}")
