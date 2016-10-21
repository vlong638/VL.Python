class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    #给一个词典，找出其中所有最长的单词
    def longestWords(self, set):
        # write your code here
        maxLength=0
        maxLetters=[]
        for key in set:
            if len(key)>maxLength:
                maxLength=len(key)
                maxLetters=[key]
            elif len(key)==maxLength:
                maxLetters.append(key)
        return maxLetters
            
    
s=Solution()
result= s.longestWords({
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
})
print(result)
