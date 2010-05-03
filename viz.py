from treecyk import CYKChart


def genDot(C,filename=None):
    if filename==None:
        filename="testfile.dot"
    specFile=""
    for key in C.graph.keys():
        for i in C.graph[key]:
            specFile+='    "%s" -> "%s" ; \n'%(key,i)
    for key in C.graph.keys():
        lable=C.chart[key[0]][key[1]]
        specFile+='    "%s"[lable = "%s"] ;\n'%(key,lable )
    finalFile=open(filename,'w')
    finalFile.write("digraph G { \n")
    finalFile.write(specFile)
    finalFile.write("}")
