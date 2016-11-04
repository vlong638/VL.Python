"""
给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

 注意事项

一个单词的界定是，由字母组成，但不包含任何的空格。
"""
class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        lastword=[]
        i=0
        seperator=" "
        prechar=" "
        while i<len(s):
            if s[i]!=seperator:
                if prechar==seperator:
                    lastword=[s[i]]
                else:
                    lastword.append(s[i])
            prechar=s[i]
            i+=1
        print(lastword)
        return len(lastword)
                    


        
s=Solution()
result= s.lengthOfLastWord("abcd1 2345 678 9")
print(type(result))
print(result)
