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
    #枚举
    def trailingZeros2(self, n):
         i = 1
         while n > 0:
             i = i * n
             n-=1
         s = str(i)
         index = len(s) - 1
         zeroCount = 0
         while index >= 0:
             if(s[index] == "0"):
                 zeroCount+=1
             else:
                 break
             index-=1
         return zeroCount
    #枚举2
    def trailingZeros(self, n):
         zeroCount = 0
         i = 1
         while n > 0:
            i = i * n
            s = str(i)
            #print()
            #print(n)
            index = len(s) - 1
            pre = zeroCount
            while index >= 0:
                if(s[index] == "0"):
                    zeroCount+=1
                    #print("+1")
                else:
                    break
                index-=1
            #print(s[0:len(s)-(zeroCount-pre)])
            i = int(s[0:len(s) - (zeroCount - pre)])
            n-=1
         return zeroCount
    #数理优化
    #5 25        125
    #a=1 b=3*a+(a+1) c=3*b+(b+1)
    #节点是*5 10 15 20 **25 30 35 40...120 ***125
    def trailingZerosByLevel(self, n):
        if n<5:
            return 0
        else:
            level=self.getLevel(n)
            return self.getByLevel(level,n)

    def getLevel(self,n):
        level=0
        current=5
        while n>current:
            current*=5
            level+=1
        return level

    def getByLevel(self,level,n):
        if level==0:
            return 1
        else:
            base=5**level
            times=int(n/base)
            #print("n",n,"times",times,"base",base)
            if times==5:
                result=times*self.getByLevel(level-1,base)+1
            else:
                result=times*self.getByLevel(level-1,base)
            if n>base*times:
                #print("+(n-base*times)",n-base*times)
                result+=self.trailingZerosByLevel(n-base*times)
            return result
        
    
            
PrintHelper.PrintCode('s=Solution()')
PrintHelper.PrintCode('print(s.trailingZeros(12))')
s=Solution()
print(s.trailingZeros(100))
print(s.trailingZerosByLevel(100))
print()
print(s.trailingZeros(200))
print(s.trailingZerosByLevel(200))
print()
print(s.trailingZeros(300))
print(s.trailingZerosByLevel(300))
print()
