import PrintHelper
class Solution:
    def strStr(self, source, target):
        if(len(source)==0 or len(target)==0):
            return -1
        i=0
        while i<len(source):
            j=0
            while j<len(target) and i+j<len(source):
                if source[i+j]==target[j]:
                    print("source",source[i+j])
                    print("target",target[j])
                    j+=1
                    if j==(len(target)):
                        return i
                else:
                    break;
            i+=1
        return -1

s=Solution()
result= s.strStr("","")
print(type(result))
print(result)


PrintHelper.PrintCode('s=Solution()')
s=Solution()
PrintHelper.PrintCode('a=\"abcd123456789\"')
a="abcd123456789"
PrintHelper.PrintCode('b=\"123\"')
b="123"
PrintHelper.PrintCode('print(\"paramA:\",a)')
print("paramA:",a)
PrintHelper.PrintCode('print(\"paramB:\",b)')
print("paramB:",b)
PrintHelper.PrintCode('result= s.strStr(a,b)')
result= s.strStr(a,b)
PrintHelper.PrintCode('print(type(result))')
print(type(result))
PrintHelper.PrintCode('print(result)')
print(result)
