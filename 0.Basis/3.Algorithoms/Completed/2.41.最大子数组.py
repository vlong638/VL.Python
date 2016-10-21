#这题的核心思路是基于线性的认知,动态规划
#尝试使用分治法求解的方式中都采用了线性的动态规划

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write you code here
        if nums==None and len(nums)==1:
            return nums
        maxSum=nums[0]
        maxArray=[nums[0]]
        curSum=0
        curArray=[]
        for num in nums:
            curSum+=num
            curArray.append(num)
            if curSum>maxSum:
                maxSum=curSum
                maxArray=curArray
            elif curSum<0:
                curSum=0
                curArray=[]
        return maxSum,maxArray
                
        
s=Solution()
resultSum,resultArray= s.maxSubArray([-2,2,-3,4,-1,2,1,-5,3])

print(resultSum)
for num in resultArray:
    print(num,end=",")
