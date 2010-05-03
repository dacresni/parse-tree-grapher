from treecyk import CYKChart

def genTree(C,start):
    mapping={ }
    for key in C.graph[start]:
        mapping.setdefault(key,[]).extend(C.graph[key])
        for i in C.graph[key]:
            if C.graph.has_key(i):
                genTree(C,i)
            else:
                mapping[i]=C.string[i[1]] #not so sure, if wrong try i[0]
    return mapping 

def genDot(C,filename=None):
    if filename==None:
        filename="testfile.dot"
    specFile=""
    cleanMapping = genTree(C,(1,len(C)-1))

    for key in cleanMapping.keys():
        if hasattr(cleanMapping[key], '__iter__') :
            for i in cleanMapping[key]:
                lable=C.chart[key[0]][key[1]] #to find number of matches
                if len(lable)!=0:
                    specFile+='    "%s" -> "%s" ; \n'%(key,i)
        else:
            specFile+='   "%s"[lebel= "%s"] ;\n'%(key,cleanMapping[key])

    for key in C.graph.keys():
        lable=C.chart[key[0]][key[1]]
        if len(lable)!=0:
            specFile+='    "%s"[label = "%s"] ;\n'%(key,lable )
    #for i in range(len(C)):
    #    lable=C.chart[i][1]
    #    specFile+='    "%s"[label = "%s"] ;\n'%((i,1),lable)
       
    finalFile=open(filename,'w')
    finalFile.write("digraph G { \n")
    finalFile.write(specFile)
    finalFile.write("}")
