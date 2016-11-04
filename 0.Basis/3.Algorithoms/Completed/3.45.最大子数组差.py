"""
给定一个整数数组，找出两个不重叠的子数组A和B
，使两个子数组和的差的绝对值|SUM(A) - SUM(B)|最大。

返回这个最大的差值。

 注意事项

子数组最少包含一个数
"""
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        n = len(nums)
        mx1 = [0]*n
        mx1[0] = nums[0]
        mn1 = [0]*n
        mn1[0] = nums[0]
        forward = [mn1[0], mx1[0]]
        array_f = [0]*n
        array_f[0] = forward[:]
        for i in range(1, n):
            mx1[i] = max(mx1[i-1] + nums[i], nums[i])
            mn1[i] = min(mn1[i-1] + nums[i], nums[i])
            forward = [min(mn1[i], forward[0]), max(mx1[i], forward[1])]
            array_f[i] = forward[:]
        mx2 = [0]*n
        mx2[n-1] = nums[n-1]
        mn2 = [0]*n
        mn2[n-1] = nums[n-1]
        backward = [mn2[n-1], mx2[n-1]]
        array_b = [0]*n
        array_b[n-1] = backward[:] 
        for i in range(n-2, -1, -1):
            mx2[i] = max(mx2[i+1] + nums[i], nums[i])
            mn2[i] = min(mn2[i+1] + nums[i], nums[i])
            backward = [min(mn2[i], backward[0]), max(mx2[i], backward[1])]
            array_b[i] = backward[:]
        result = -65535
        for i in range(n-1):
            result = max(result, abs(array_f[i][0] - array_b[i+1][1]), abs(array_f[i][1] - array_b[i+1][0]))
        return result

s=Solution()
from InputHelper import FileReader
f=FileReader()
result= s.maxDiffSubArrays(f.ReadIntList("C:\\Users\\dcw027\\Desktop\\ins\\11.in"))
print(type(result))
print(result)

"""
result= s.maxDiffSubArrays([1, 2, -3, 1])
print(type(result))
print(result)

from InputHelper import FileReader
f=FileReader()
result= s.maxDiffSubArrays(f.ReadIntList("C:\\Users\\dcw027\\Desktop\\ins\\10.in"))
print(type(result))
print(result)
"""

"""

    def maxDiffSubArrays(self, nums):
        if len(nums)<=1:
            return 0
        if len(nums)==2:
            return abs(nums[0]-nums[1])
            
        print("nums",len(nums),nums[len(nums)-1])
        result=0
        sum1,array1,start1,end1=self.maxSubArray(nums)
        print("sum1",sum1,start1,end1)
        if start1==0 and end1==len(nums)-1:

            
            result=max(result,abs(sum1-nums[0]*2),abs(sum1-nums[len(nums)-1]*2))
        if start1!=end1:
            subSum1,subArray1,subStart1,subEnd1=self.minSubArray(nums[start1:end1])
            print("subSum1",subSum1,subStart1,subEnd1)
            if subStart1!=0:
                subSum2,subArray2,subStart2,subEnd2=self.maxSubArray(array1[0:subStart1])
                result=max(result,abs(subSum2-subSum1))
                print("subSum2",subSum2,subStart2,subEnd2)
            if subEnd1+1!=len(array1):
                subSum3,subArray3,subStart3,subEnd3=self.maxSubArray(array1[subEnd1+1:len(array1)])
                result=max(result,abs(subSum3-subSum1))
                print("subSum3",subSum3,subStart3,subEnd3)
        if 0!=start1:
            sum2,array2,start2,end2=self.minSubArray(nums[0:start1])
            if start1==end1:
                result=max(result,abs(sum1-sum2))
            else:
                result=max(result,abs(sum1-sum2))
            print("sum2",sum2,start2,end2)
        if end1+1!=len(nums):
            sum3,array3,start3,end3=self.minSubArray(nums[end1+1:])
            if start1==end1:
                result=max(result,abs(sum1-sum3))
            else:
                result=max(result,abs(sum1-sum3))
            print("sum3",sum3,start3,end3)
        
        sum1,array1,start1,end1=self.minSubArray(nums)
        print("sum1",sum1,start1,end1)
        if start1==0 and end1==len(nums)-1:
            result=max(result,abs(sum1-nums[0]*2),abs(sum1-nums[len(nums)-1]*2))
        if start1!=end1:
            subSum1,subArray1,subStart1,subEnd1=self.maxSubArray(nums[start1:end1])
            print("subSum1",subSum1,subStart1,subEnd1)
            if subStart1!=0:
                subSum2,subArray2,subStart2,subEnd2=self.maxSubArray(array1[0:subStart1])
                result=max(result,abs(subSum2-subSum1))
                print("subSum2",subSum2,subStart2,subEnd2)
            if subEnd1+1!=len(array1):
                subSum3,subArray3,subStart3,subEnd3=self.minSubArray(array1[subEnd1+1:len(array1)])
                result=max(result,abs(subSum3-subSum1))
                print("subSum3",subSum3,subStart3,subEnd3)
        if 0!=start1:
            sum2,array2,start2,end2=self.maxSubArray(nums[0:start1])
            if start1==end1:
                result=max(result,abs(sum1-sum2))
            else:
                result=max(result,abs(sum1-sum2))
            print("sum2",sum2,start2,end2)
        if end1+1!=len(nums):
            sum3,array3,start3,end3=self.maxSubArray(nums[end1+1:])
            if start1==end1:
                result=max(result,abs(sum1-sum3))
            else:
                result=max(result,abs(sum1-sum3))
            print("sum3",sum3,start3,end3)
        return result
    
    def minSubArray(self, nums):
        #print("nums",nums)
        if nums==None or len(nums)==0:
            return 0,nums,0,0
        minSum=nums[0]
        minArray=[nums[0]]
        curSum=0
        curArray=[]
        minstart=0
        minend=0
        index=0
        start=index
        for num in nums:
            curSum+=num
            if curSum<minSum and curSum<0:
                curArray.append(num)
                #print("append",num)
                minSum=curSum
                minArray=curArray
                minstart=start
                minend=index
            elif curSum<minSum and curSum>=0:
                curSum=num
                curArray=[num]
                start=index
                #print("reset",num)
                minSum=curSum
                minArray=curArray
                minstart=start
                minend=index
            elif curSum>0:
                #print("reset",num)
                curSum=0
                curArray=[]
                start=index+1
            else:
                curArray.append(num)
                #print("append",num)
            index+=1
        return minSum,minArray,minstart,minend
    
    def maxSubArray(self, nums):
        #print("nums",nums)
        if nums==None or len(nums)==0:
            return 0,nums,0,0
        maxSum=nums[0]
        maxArray=[nums[0]]
        curSum=0
        curArray=[]
        maxstart=0
        maxend=0
        index=0
        start=index
        for num in nums:
            curSum+=num
            if curSum>maxSum and curSum>0:
                curArray.append(num)
                #print("append",num)
                maxSum=curSum
                maxArray=curArray
                maxstart=start
                maxend=index
            elif curSum>maxSum and curSum<=0:
                curSum=num
                curArray=[num]
                start=index
                #print("reset",num)
                maxSum=curSum
                maxArray=curArray
                maxstart=start
                maxend=index
            elif curSum<0:
                #print("reset",num)
                curSum=0
                curArray=[]
                start=index+1
            else:
                curArray.append(num)
                #print("append",num)
            index+=1
        return maxSum,maxArray,maxstart,maxend
"""
