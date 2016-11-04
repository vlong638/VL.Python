class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    #将一个字符串中的所有空格替换成 %20 。
    #你可以假设该字符串有足够的空间来加入新的字符，
    #且你得到的是“真实的”字符长度。
    #你的程序还需要返回被替换后的字符串的长度。
    def replaceBlank(self, string, length):
        # Write your code here
        index=0
        newString=[]
        while index<length:
            letter=string[index]
            if letter==" ":
                string[index]="%20"
                newString.extend(["%","2","0"])
            else:
                newString.append(letter)
            index+=1
        return "".join(newString)
                
                
                


        
s=Solution()
result= s.replaceBlank("Mr John Smith",13)
print(type(result))
print(result)
