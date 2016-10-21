#这题的核心思路是基于线性的认知,动态规划
#尝试使用分治法求解的方式中都采用了线性的动态规划
from copy import deepcopy
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write you code here
        if nums==None and len(nums)==1:
            return nums
        minSum=nums[0]
        minArray=[nums[0]]
        curSum=0
        curArray=[]
        for num in nums:
            curSum+=num
            curArray.append(num)
            print("curArray.append",num)
            
            if curSum<minSum:
                print("curSum<minSum minSum=curSum")
                minSum=curSum
                minArray=deepcopy(curArray)
            elif curSum>0:
                print("curSum>0 reset array")
                curSum=0
                curArray=[]
        return minSum,minArray

s=Solution()
resultSum,resultArray= s.minSubArray([101,33,44,55,67,78,100,200,1000,22])

print(resultSum)
for num in resultArray:
    print(num,end=" ")

