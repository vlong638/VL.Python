"""
实现一个leftpad库，如果不知道什么是leftpad可以看样例

样例
leftpad("foo", 5)
>> "  foo"

leftpad("foobar", 6)
>> "foobar"

leftpad("1", 2, "0")
>> "01"
"""
class Solution:
    # @param {string} originalStr the string we want to append to
    # @param {int} size the target length of the string
    # @param {string} padChar the character to pad to the left side of the string
    # @return {string} a string
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # Write your code here
        l=len(originalStr)
        if l<size:
            return padChar*(size-l)+originalStr
        else:
            return originalStr
        
s=Solution()
result= s.leftPad("foo",5)
print(type(result))
print(result)
