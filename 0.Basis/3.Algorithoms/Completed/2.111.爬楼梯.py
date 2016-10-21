class Solution:
# @param s: a list of char
# @param offset: an integer 
# @return: nothing
#假设你正在爬楼梯，需要n步你才能到达顶部。
#但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？
    def climbStairs(self, n):
        # write your code here
        if n==0:
            return 0
        if n==1:
            return 1
        return self.climbStairsByStep(n)
        
    def climbStairsByStep(self,n):
        if n==0:
            return 1
        if n==1:
            return 1
        return self.climbStairsByStep(n-1)+self.climbStairsByStep(n-2)
    
s=Solution()
result= s.climbStairs(5)
print(type(result))
print(result)
