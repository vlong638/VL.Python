class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        dicA=self.StringToDic(A)
        print("dicA:",dicA)
        print("B:",B)
        if len(dicA)==0:
            return "false"
        for key in B:
            value=dicA.get(key)
            if value==None:
                return "false"
        return "true"
    
    def StringToDic(self, string):
        dic={}
        for letter in string:
            value=dic.get(letter)
            if value == None:
                dic[letter]=1
        return dic



        
s=Solution()
result= s.compareStrings("","A")
print(type(result))
print(result)
