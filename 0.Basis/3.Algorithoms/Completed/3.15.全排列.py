"""
给定一个数字列表，返回其所有可能的排列。

 注意事项

你可以假设没有重复数字。
"""
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    #递归
    def permute(self, nums):
        # write your code here
        if len(nums)==0:
            return [[]]
        
        result=[]
        self.permuteWithResult(nums,[],result)
        return result
        
    def permuteWithResult(self,nums,current,result):
        if len(nums)==1:
            current.append(nums[0])
            result.append(current)
        else:
            index=0
            length=len(nums)-1
            while index<=length:
                newCurrent=current[:]
                newNums=nums[:]
                newCurrent.append(newNums.pop(index))
                self.permuteWithResult(newNums,newCurrent,result)
                index+=1
                

    
s=Solution()
result= s.permute([1,2,3,4])
for line in result:
    print(line)

