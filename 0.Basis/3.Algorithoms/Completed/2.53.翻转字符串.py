class Solution:
    # @param s : A string
    # @return : A string
    #摘词
    #倒置
    #拼接
    def reverseWords(self, s):
        # write your code here
        #摘词
        words=[]
        word=[]
        letterIndex=0
        for letter in s:
            if letter==" ":
                if len(word)>0:
                    value="".join(word)
                    words.append(value)
                    word=[]
                    print("words.append",value)
            else:
                word.append(letter)
                print("word.append",letter)                
            letterIndex+=1
            print(letterIndex,len(s))
            if letterIndex==len(s):
                value="".join(word)
                words.append(value)
                print("words.append",value)
        #倒置
        reversedWords=[]
        while len(words)>0:
            reversedWords.append(words.pop())
        #拼接,并移除空格
        return (" ".join(reversedWords)).lstrip()
s=Solution()
result= s.reverseWords( "the sky is blue   ")
for letter in result:
    print("letter",letter)
