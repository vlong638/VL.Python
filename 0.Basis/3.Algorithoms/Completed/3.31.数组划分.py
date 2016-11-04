"""
给出一个整数数组 nums 和一个整数 k。
划分数组（即移动数组 nums 中的元素），使得：

所有小于k的元素移到左边
所有大于等于k的元素移到右边
返回数组划分的位置，即数组中第一个位置 i，满足 nums[i] 大于等于 k。

 注意事项

你应该真正的划分数组 nums，而不仅仅只是计算比 k 小的整数数
，如果数组 nums 中的所有元素都比 k 小，则返回 nums.length。
"""
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        x=0
        y=len(nums)-1
        index=len(nums)
        while x<len(nums) and x<y:
            if nums[x]>=k:
                print("find x:{} at index:{}".format(nums[x],x))
                index=x
                while y>=0 and x<y:
                    if nums[y]<k:
                        print("find y:{} at index:{}".format(nums[y],y))
                        temp=nums[y]
                        nums[y]=nums[x]
                        nums[x]=temp
                        index=y
                        break
                    y-=1
            x+=1
        print(nums)
        return index

s=Solution()
result= s.partitionArray([9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9], 9)
print(type(result))
print(result)
