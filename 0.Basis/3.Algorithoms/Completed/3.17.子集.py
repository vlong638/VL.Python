"""
给定一个含不同整数的集合，返回其所有的子集

 注意事项

子集中的元素排列必须是非降序的，解集必须不包含重复的子集
"""
class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, nums):
        self.result=[]
        self.search(sorted(nums),[],0)
        return self.result

    def search(self,nums,subset,index):
        if index==len(nums):
            self.result.append(subset)
            return

        self.search(nums,subset+[nums[index]],index+1)
        self.search(nums,subset,index+1)
        
            
        


s=Solution()
result= s.subsets([1,2,3])
print(type(result))
print(result)
