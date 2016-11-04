class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
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
    def trailingZeros(self, n):
         zeroCount = 0
         i = 1
         while n > 0:
            i = i * n
            s = str(i)
            index = len(s) - 1
            pre = zeroCount
            while index >= 0:
                if(s[index] == "0"):
                    zeroCount+=1
                else:
                    break
                index-=1
            #print(s[0:len(s)-(zeroCount-pre)])
            i = int(s[0:len(s) - (zeroCount - pre)])
            n-=1
         return zeroCount
    def trailingZerosByLevel(self, n):
        if n<5:
            return 0
        else:
            level=self.getLevel(n)
            return self.getByLevel(level,n)

    def getLevel(self,n):
        level=1
        current=5
        while n>current:
            current*=5
            level+=1
        return level

    def getByLevel(self,level,n):
        if level==1:
            return 1
        else:
            base=5**level
            times=int(n/base)
            result=times*self.getByLevel(level-1,base)
            if n>base*times:
                result+=self.trailingZerosByLevel(n-base*times)
            return result