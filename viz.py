from cyk import CYKChart
class genVIZ(object):
    def __init__(self,C,filename=None):
        if filename==None:
            self.filename="testfile.dot"
        else:
            self.filename=filename

    def genTree(self,G,here,visited):
        neighbors=G
        if not here in visited:
            visited.add(here)
            if neighbors.has_key(here):  # if it has neighbors
                for next in neighbors[here]:
                    self.edges.append((here,next))
                    self.specFile+='  "%s" -> "%s" ;\n'%((here,next ))
                    self.genTree(G,next,visited)

    def genDot(self, C):
        self.specFile=""
        self.edges=[]
        self.visited = set()
        print C.graph
        if not C.graph.has_key((1,len(C)-1)):
            raise Exception("parse error")
        self.genTree(C.graph, (1,len(C)-1),self.visited )
        for node in self.visited :
            lable=C.chart[node[0]][node[1]]
            self.specFile+='    "%s"[label = "%s"] ;\n'%(node,list(lable )) 
            #find lable for leaf node 
        finalFile=open(self.filename,'w')
        finalFile.write("digraph G { \n")
        finalFile.write(self.specFile)
        finalFile.write("}")
        
    def genJS(self, C):
        self.specFile=""
        self.edges=[]
        self.visited=set()
        if (1,len(C)-1) not in C.graph.keys():
            raise Exception("parse error")
        self.genJSTree(C.graph, (1,len(C)-1),self.visited)
        for node in self.visited :
            lable=C.chart[node[0]][node[1]]
            self.specFile+='    "g.addNode(%s", {label:"%s"} );\n'%(node,list(lable )) 
        #find lable for leaf node 
        finalFile=open(self.filename,'w')
        finalFile.write("var g = new Graph();  \n")
        finalFile.write(self.specFile)
        ending = \
        """
        var layouter = new Graph.Layout.Spring(g);
        layouter.layout();

        var renderer = new Graph.Renderer.Raphael('canvas',g,400,300);
        renderer.draw();
        """
        finalFile.write(ending)

    def genJSTree(self,G,here,visited):
        neighbors=G
        if not here in visited:
            visited.add(here)
            if neighbors.has_key(here):  # if it has neighbors
                for next in neighbors[here]:
                    self.edges.append((here,next))
                    self.specFile+='g.addEdge("%s","%s");\n'%((here,next ))
                    self.genJSTree(G,next,visited)

