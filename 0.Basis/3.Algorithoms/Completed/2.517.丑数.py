"""
写一个程序来检测一个整数是不是丑数。

丑数的定义是，只包含质因子 2, 3, 5 的正整数。
比如 6, 8 就是丑数，但是 14 不是丑数以为他包含了质因子 7。
"""
class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        if num==0:
            return False
        if num==1:
            return True
        else:
            if num%2==0:
                return self.isUgly(num/2)
            if num%3==0:
                return self.isUgly(num/3)
            if num%5==0:
                return self.isUgly(num/5)
            return False
s=Solution()
result= s.isUgly(7)
print(type(result))
print(result)
result= s.isUgly(8)
print(type(result))
print(result)

