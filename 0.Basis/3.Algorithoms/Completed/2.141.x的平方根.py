class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    实现 int sqrt(int x) 函数，计算并返回 x 的平方根。
    """
    def sqrt(self, x):
        # write your code here
        if x==0:
            return 0
        print()
        times=self.searchPower(x)
        maxV=2**int(times/2+1)
        minV=2**int(times/2)
        return self.searchSqrt(x,maxV,minV)
    
    def searchPower(self,x):
        t=int(x/2)
        times=1
        while t>1:
            print("t",t)
            print("times",times)
            t=int(t/2)
            times+=1
        return times
        
    def searchSqrt(self,x,maxV,minV):
        if maxV==minV:
            print("return maxV",maxV)
            return maxV
        mid=int((maxV+minV)/2)
        if mid**2>x:
            print("mid**2>x","mid**2",mid)
            print("self.search","maxV",maxV,"minV:",minV)
            return self.searchSqrt(x,mid,minV)

        else:
            if (mid+1)**2>x:
                print("(mid+1)**2>x","(mid+1)**2",(mid+1)**2)
                print("return mid",mid)
                return mid
            return self.searchSqrt(x,maxV,mid)
            
        
        

        
s=Solution()
result= s.sqrt(4)
print(type(result))
print(result)
result= s.sqrt(5)
print(type(result))
print(result)
result= s.sqrt(999999999)
print(type(result))
print(result)
"""
    def sqrt(self, x):
        # write your code here
        if x==0:
            return 0
        print()
        t=int(x/2)
        times=1
        while t>1:
            print("t",t)
            print("times",times)
            t=int(t/2)
            times+=1
        return times
print(2**result)
print(2**(result+1))
print(2**int(result/2))
print(2**int(result/2+1))
print(31622)
"""

