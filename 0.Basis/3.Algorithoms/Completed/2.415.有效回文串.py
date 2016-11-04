import re
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    """
给定一个字符串，判断其是否为一个回文串。只包含字母和数字，忽略大小写。

 注意事项

你是否考虑过，字符串有可能是空字符串？这是面试过程中，面试官常常会问的问题。

在这个题目中，我们将空字符串判定为有效回文。
    """
    def isPalindrome(self, s):
        # Write your code here
        if len(s)==0:
            return True
        s=s.lower()
        a=0
        b=len(s)-1
        A=None
        B=None
        while a<len(s):
            if A==None:
                if self.isAlphanumericCharacter(s[a]):
                    A=a
                else:
                    a+=1
                    continue
            if B==None:
                if self.isAlphanumericCharacter(s[b]):
                    B=b
                else:
                    b-=1
                    continue
            
            if s[a]!=s[b]:
                return False
            else:
                A=None
                B=None
                a+=1
                b-=1
        return True
    

    def isAlphanumericCharacter(self,s):
        return re.compile(r"\w").search(s)


        
s=Solution()
result= s.isPalindrome("123321")
print(type(result))
print(result)
result= s.isPalindrome("a.")
print(type(result))
print(result)
