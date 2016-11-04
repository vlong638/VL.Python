class Solution:
# @param s: a list of char
# @param offset: an integer 
# @return: nothing
    def rotateString(self, s, offset):
        if len(s) == 0:
            return ""
        offset=offset%len(s)
        temp=s[len(s)-offset:]+s[:-offset]
        i=0
        while i<len(temp):
            s[i]=temp[i]
            i+=1
    
    def rotateString2(self, s, offset):
        # write you code here
        if len(s) == 0:
        result=""
        ls=list(s)
        i=0
        while i<offset:
            result+=ls.pop(0)
            i+=1
        while len(ls)>0:
            result+=ls.pop()
        return result
s=Solution()
result= s.rotateString("abcdefg", 3)
print(result)
