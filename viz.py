from treecyk import CYKChart
class genDot(object):
    def bfs(self, graph, start, path=[]):
        q=[start]
        while q:
            v=q.pop(0)
            if not v in path:
                path.append(v)
                q.append(graph[v])
        return path



    def genTree(self,C,start,path):
        if not C.graph.has_key(start):
            raise Exception("parse error")
        path.setdefault(start,[]).extend(C.graph[start])
        for key in C.graph[start]:
            if not C.graph.has_key(key): #then its a leif noad 
                lable=C.chart[key[0]][key[1]]
                self.specFile+='    "%s"[label = "%s"] ;\n'%(key,lable ) #find lable for leaf node 
            else:
                path.setdefault(key,[]).extend(C.graph[key])
                self.genTree(C,key,path)
        return path 
    def __init__(self,C,filename=None):
        if filename==None:
            self.filename="testfile.dot"
        else:
            self.filename=filename
        self.specFile=""
        print C.graph
        cleanMapping = self.genTree(C,(1,len(C)-1), { })
        print cleanMapping
        


        #for key in cleanMapping.keys():
        #        self.specFile+='    "%s" -> "%s" ; \n'%(key,cleanMapping[key][0])
        #        self.specFile+='    "%s" -> "%s" ; \n'%(key,cleanMapping[key][1])

        for key in cleanMapping.keys():
                path = []
                for i in cleanMapping[key]:
                    path.append('"(%i,%i)"'%(i[0],i[1]))
                print path
                line=" -> ".join(path)
                line+="\n"
                print line
                self.specFile+=line

        for key in C.graph.keys():
            lable=C.chart[key[0]][key[1]]
            if len(lable)!=0:
                self.specFile+='    "%s"[label = "%s"] ;\n'%(key,lable )
  
        finalFile=open(self.filename,'w')
        finalFile.write("digraph G { \n")
        finalFile.write(self.specFile)
        finalFile.write("}")
