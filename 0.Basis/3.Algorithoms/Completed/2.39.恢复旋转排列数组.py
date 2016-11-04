class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums==None:
            return nums
        if len(nums)<=1:
            return nums
        firstValue=nums.pop(0)
        temp=[firstValue]
        result=[]
        while len(nums)>0:
            if nums[0]>=firstValue:
                temp.append(nums.pop(0))
            else:
                break
        result.extend(nums)
        result.extend(temp)
        nums=result
s=Solution()
result= s.recoverRotatedSortedArray([4, 5, 1, 2, 3])
print(type(result))
print(result)
