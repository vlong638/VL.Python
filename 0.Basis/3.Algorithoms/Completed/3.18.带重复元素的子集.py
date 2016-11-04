import functools
class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    
    #1.一个偷懒的方式使用上一个"子集"的编码,增加重复检测即可
    """
    def subsetsWithDup(self,nums):
        self.result=[]
        self.search(sorted(nums),[],0)
        return self.result

    def search(self,nums,subset,index):
        if index==len(nums):
            if subset not in self.result:
                self.result.append(subset)
            return

        self.search(nums,subset+[nums[index]],index+1)
        self.search(nums,subset,index+1)
    """
    #2非递归的解决方案,需应用functools.reduce(@func,@params)
    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        p = [[nums[x]
              for x in range(len(nums))
              if i>>x&1
              ]
              for i in range(2**len(nums))
            ]
        p = functools.reduce(lambda x,y:x if y in x else x + [y], [[]] + p)
        return list(reversed(p))
  


s=Solution()
result= s.subsetsWithDup([1,2,2,3])
print(type(result))
print(result)
