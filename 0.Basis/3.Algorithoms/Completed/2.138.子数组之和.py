class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    给定一个整数数组，找到和为零的子数组。
    你的代码应该返回满足要求的子数组的起始位置和结束位置
    """

    def subarraySum(self, nums):
        # write your code here
        x=0
        maxX=len(nums)-1
        while x<=maxX:
            value=nums[x]
            if value==0:
                return [x,x]
            print()
            print("reset x:",value)
            y=x+1
            while y<=maxX:
                value+=nums[y]
                print("append y:",nums[y])
                if value==0:
                    return [x,y]
                y+=1
            x+=1
        return None




        
s=Solution()
result= s.subarraySum([4,10,13,4,-1,0,3,3,5])
print(type(result))
print(result)
