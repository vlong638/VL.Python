import collections
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        if len(nums)==0:
            return [[]]

        counter=collections.Counter(nums)
        dic={}
        for item in counter:
            dic[item]=counter[item]

        result=[]
        self.permuteUniqueWithResult(dic,[],result)
        return result
        
    def permuteUniqueWithResult(self,dic,current,result):
        if len(dic)==1:
            for letter in dic:
                newDic=dic.copy()
                while newDic[letter]>0:
                    current.append(letter)
                    newDic[letter]-=1
            result.append(current)
        else:
            for letter in dic:
                newCur=current[:]
                newDic=dic.copy()
                newCur.append(letter)
                newDic[letter]-=1
                if newDic[letter]==0:
                    del(newDic[letter])
                self.permuteUniqueWithResult(newDic,newCur,result)
            
        
        


        
s=Solution()
result= s.permuteUnique([1,2,2])
print(result)
