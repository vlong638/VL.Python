import PrintHelper
PrintHelper.PrintCode('class Solution:')
PrintHelper.PrintCode(' # @param n a integer')
PrintHelper.PrintCode(' # @return ans a integer')
PrintHelper.PrintCode(' def trailingZeros(self, n):')
PrintHelper.PrintCode('     i=1')
PrintHelper.PrintCode('     while n>0:')
PrintHelper.PrintCode('         i=i*n')
PrintHelper.PrintCode('         n-=1')
PrintHelper.PrintCode('     print(i)')
PrintHelper.PrintCode('     s=str(i)')
PrintHelper.PrintCode('     index=len(s)-1')
PrintHelper.PrintCode('     zeroCount=0')
PrintHelper.PrintCode('     while index>=0:')
PrintHelper.PrintCode('         if(s[index]==\"0\"):')
PrintHelper.PrintCode('             zeroCount+=1')
PrintHelper.PrintCode('         else:')
PrintHelper.PrintCode('             break')
PrintHelper.PrintCode('         index-=1')
PrintHelper.PrintCode('     return zeroCount')
class Solution:
 # @param n a integer
 # @return ans a integer
 def trailingZeros(self, n):
     i=1
     while n>0:
         i=i*n
         n-=1
     print(i)
     s=str(i)
     index=len(s)-1
     zeroCount=0
     while index>=0:
         if(s[index]=="0"):
             zeroCount+=1
         else:
             break
         index-=1
     return zeroCount
PrintHelper.PrintCode('s=Solution()')
PrintHelper.PrintCode('print(s.trailingZeros(12))')
s=Solution()
print(s.trailingZeros(12))
