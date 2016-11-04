"""
from InputHelper import FileReader
f=FileReader()
f.ReadList(@path)
"""

class FileReader:
    
    def ReadIntList(self,path):
        with open(path) as fp:
            buffer=fp.read()
            strings=buffer.replace("[","")
            strings=strings.replace("]","")
        result=[]
        for string in strings.split(","):
            result.append(int(string))
        return result
    
    def ReadTreeNodes(self,path):
        pass
    
    def ReadLinkList(self,path):
        pass
