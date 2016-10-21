class Solution:
    """
    @param n: An integer
    @return: True or false
    用 O(1) 时间检测整数 n 是否是 2 的幂次
    """
    def checkPowerOf2(self, x):
        # write your code here
        if x==0:
            return False
        if x==1:
            return True
        print()
        times=self.searchPower(x)
        if 2**times==x:
            return True
        else:
            return False
    
    def searchPower(self,x):
        t=int(x/2)
        times=1
        while t>1:
            print("t",t)
            print("times",times)
            t=int(t/2)
            times+=1
        return times
        
        

        
s=Solution()
result= s.checkPowerOf2(4)
print(result)

result= s.checkPowerOf2(8)
print(result)

result= s.checkPowerOf2(44)
print(result)

result= s.checkPowerOf2(444)
print(result)

result= s.checkPowerOf2(1)
print(result)

