from treecyk import CYKChart
"""
def genTree(C,start):
    mapping={ }
    for key in C.graph[start]:
        mapping.setdefault(key,[]).extend(C.graph[key])
        for i in C.graph[key]:
            if C.graph.has_key(i):
                genTree(C,i)
            else:
                mapping.setdefault(i,[]).append(C.string[i[1]])  #not so sure, if wrong try i[0]
    return mapping 
"""

class genDot(object):
    def genTree(self,C,start):
        mapping={ }
        if not C.graph.has_key(start):
            raise Exception("parse error")
        mapping.setdefault(start,[]).extend(C.graph[start])
        for key in C.graph[start]:
            if not C.graph.has_key(key):
                #mapping.setdefault(i,[]).append(C.string[i[1]])  #not so sure, if wrong try i[0]
                pass
            else:
                mapping.setdefault(key,[]).extend(C.graph[key])
                for i in C.graph[key]:
                    if C.graph.has_key(i):
                        self.genTree(C,i)
        return mapping 
    def __init__(self,C,filename=None):
    #def genDot(C,filename=None):
        if filename==None:
            self.filename="testfile.dot"
        else:
            self.filename=filename
        self.specFile=""
        cleanMapping = self.genTree(C,(1,len(C)-1))

        for key in cleanMapping.keys():
            #if hasattr(cleanMapping[key], '__iter__') :
                for i in cleanMapping[key]:
                    lable=C.chart[key[0]][key[1]] #to find number of matches
                    if len(lable)!=0:
                        self.specFile+='    "%s" -> "%s" ; \n'%(key,i)

        for key in C.graph.keys():
            lable=C.chart[key[0]][key[1]]
            if len(lable)!=0:
                self.specFile+='    "%s"[label = "%s"] ;\n'%(key,lable )
        for i in range(1,len(C)):
            self.specFile+='    "%s"[label= "%s"] ;\n'%((i,1),C.chart[i][1])
  
        finalFile=open(self.filename,'w')
        finalFile.write("digraph G { \n")
        finalFile.write(self.specFile)
        finalFile.write("}")
