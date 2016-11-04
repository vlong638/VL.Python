class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    """
    给定两个二进制字符串，返回他们的和（用二进制表示）。
    """
    def addBinary(self, a, b):
        # Write your code here
        a=int(a,2)
        b=int(b,2)
        print(a,b)
        return bin(self.binarySum(a,b))[2:]

    def binarySum(self,a,b):
        c=a^b
        carry=(a&b)<<1
        print(bin(a),bin(b))
        print(bin(c),bin(carry))
        print()
        if carry>0:
            return self.binarySum(c,carry)
        else:
            return c
        



        
s=Solution()
result= s.addBinary("11","1")
print(type(result))
print(result)
