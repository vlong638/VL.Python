import PrintHelper
PrintHelper.PrintCode('class Solution:')
PrintHelper.PrintCode('# @param s: a list of char')
PrintHelper.PrintCode('# @param offset: an integer ')
PrintHelper.PrintCode('# @return: nothing')
PrintHelper.PrintCode('    def rotateString(self, s, offset):')
PrintHelper.PrintCode('        # write you code here')
PrintHelper.PrintCode('        result=\"\"')
PrintHelper.PrintCode('        ls=list(s)')
PrintHelper.PrintCode('        i=0')
PrintHelper.PrintCode('        while i<offset:')
PrintHelper.PrintCode('            result+=ls.pop(0)')
PrintHelper.PrintCode('            i+=1')
PrintHelper.PrintCode('        while len(ls)>0:')
PrintHelper.PrintCode('            result+=ls.pop()')
PrintHelper.PrintCode('        return result')
class Solution:
# @param s: a list of char
# @param offset: an integer 
# @return: nothing
    def rotateString(self, s, offset):
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
PrintHelper.PrintCode('s=Solution()')
s=Solution()
PrintHelper.PrintCode('result= s.rotateString(\"abcd123456789\",2)')
result= s.rotateString("abcd123456789",2)
PrintHelper.PrintCode('print(type(result))')
print(type(result))
PrintHelper.PrintCode('print(result)')
print(result)
