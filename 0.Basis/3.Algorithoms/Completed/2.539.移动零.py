"""
给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序

 注意事项

1.必须在原数组上操作
2.最小化操作数
"""
class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        i=0
        while i<len(nums):
            if nums[i]==0:
                j=i+1
                while j<len(nums):
                    if nums[j]!=0:
                        temp=nums[j]
                        nums[j]=nums[i]
                        nums[i]=temp
                        break
                    j+=1
            i+=1
        return nums
s=Solution()
result= s.moveZeroes([0, 1, 0, 3, 12])
print(type(result))
print(result)
