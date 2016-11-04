"""
我们有一个栅栏，它有n个柱子，现在要给柱子染色，有k种颜色可以染。
须保证最多只有两个相邻的柱子颜色相同，求有多少种染色方案。
"""
class Solution:
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways

    def numWays(self, n, k):  
        if n == 0 or k == 0:  
            return 0
        record = [k, k * k]  
        index = 2  
        while index < n:
            record.append(record[-1] * (k - 1) + record[-2] * (k - 1))  
            index += 1  
        print()
        print("n",n,"k",k)
        print(record)
        return record[n - 1]
    
s=Solution()
result= s.numWays(3,2)
print(result)
result= s.numWays(1,5)
print(result)
result= s.numWays(5,1)
print(result)
