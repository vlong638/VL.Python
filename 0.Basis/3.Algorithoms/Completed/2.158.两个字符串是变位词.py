class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    写出一个函数 anagram(s, t)
    判断两个字符串是否可以通过改变字母的顺序变成一样的字符串。
    """
    def anagram(self, s, t):
        # write your code here
        sDic=self.toDictionary(s)
        tDic=self.toDictionary(t)
        for itemS in sDic.items():
            valueT=tDic.get(itemS[0])
            if valueT==None or valueT!=itemS[1]:
                return False
        return True

    def toDictionary(self,s):
        dic={}
        for letter in s:
            if dic.get(letter):
                dic[letter]+=1
            else:
                dic[letter]=1
        return dic
    
s=Solution()
result= s.anagram("abcd123456789","abcd12345679")
print(type(result))
print(result)
