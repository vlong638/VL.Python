"""
计算数字k在0到n中的出现的次数，k可能是0~9的一个值
"""
class Solution:
 # @param k & n two integer
 # @return ans a integer
 def digitCounts(self, k, n):
     count=0
     x=0
     while x<=n:
         for letter in str(x):
             if k==int(letter):
                 count+=1             
         x+=1
     return count
     
s=Solution()
result= s.digitCounts(1,10)
print(type(result))
print(result)
