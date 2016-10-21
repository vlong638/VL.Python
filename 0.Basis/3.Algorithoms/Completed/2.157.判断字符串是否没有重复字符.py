class Solution:
    # @param s: a string
    # @return: a boolean
    #实现一个算法确定字符串中的字符是否均唯一出现
    def isUnique(self, str):
        # write your code here
        set={""}
        for letter in str:
            if letter not in set:
                print("letter not in set:",letter)
                set.add(letter)
            else:
                return False
        return True
        
        
s=Solution()
result=s.isUnique("abc")
print(result)
