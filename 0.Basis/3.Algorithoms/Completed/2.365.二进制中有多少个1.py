class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    #计算在一个 32 位的整数的二进制表式中有多少个 1.
    #上述二进制指计算机所存储的二进制,对于负数则是反码
    def countOnes(self, num):
        # write your code here
        if num<0:
            count=1
            num-=1
            num=2**31-1^num
            num=-num
        else:
            count=0
        for letter in bin(num):
            print(letter,end="")
            if letter=="1":
                count+=1
        return count
            

s=Solution()
result= s.countOnes(-1)
print(type(result))
print(result)
