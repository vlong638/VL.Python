class Solution:
# @param s: a list of char
# @param offset: an integer 
# @return: nothing
    def fizzBuzz(self, n):
        # write you code here
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
result= s.rotateString("abcd123456789",2)
print(type(result))
print(result)
