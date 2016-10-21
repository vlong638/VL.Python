class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        if nums==None:
            return None     
        nums.sort()
        if len(nums)%2==1:
            return nums[int(len(nums)/2)]
        else:
            return nums[int(len(nums)/2)-1]
        
s=Solution()
result= s.median([4, 5, 1, 2, 3])
print(type(result))
print(result)
result= s.median([7, 9, 4, 5])
print(type(result))
print(result)
