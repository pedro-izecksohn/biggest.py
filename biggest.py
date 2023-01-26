#!/usr/bin/python3
import os
import sys

class FileNameSize:
    def __init__(self, name, size):
        self.name=name
        self.size=size
    def __eq__(self,other):
        return self.size==other.size
    def __gt__(self,other):
        return self.size>other.size
    def __lt__(self,other):
        return self.size<other.size

def searchDir (d):
    realDir=os.scandir(d)
    ret=[]
    for element in realDir:
        if element.is_file():
            ret.append(FileNameSize(element.path,element.stat().st_size))
        elif element.is_dir():
            ret.extend(searchDir(element.path))
    return ret

nresults=10
if len(sys.argv)==2:
    nresults=int(sys.argv[1])
lresults=searchDir(os.getcwd())
lresults.sort()
lresults.reverse()
lresults=lresults[:nresults]
for fns in lresults:
    print(str(fns.size)+"\t"+fns.name)
