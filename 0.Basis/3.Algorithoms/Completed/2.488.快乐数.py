"""
写一个算法来判断一个数是不是"快乐数"。

一个数是不是快乐是这么定义的：对于一个正整数，
每一次将该数替换为他每个位置上的数字的平方和，
然后重复这个过程直到这个数变为1，或是无限循环但始终变不到1。
如果可以变为1，那么这个数就是快乐数。
"""
class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        while n!=1:
            print(n)
            if(n==4):
                return False
            n=self.getNext(n)
        return True

    def getNext(self,seed):
        sum=0
        for letter in str(seed):
            sum+=int(letter)**2
        return sum
        
                
        

        
s=Solution()
result= s.isHappy(2)
print(type(result))
print(result)

result= s.isHappy(55)
print(type(result))
print(result)
