class Solution:
    # @param nums: a list of integers
    # @return: nothing
    #分割一个整数数组，使得奇数在前偶数在后。
    def partitionArray(self, nums):        
        #方案一 利用额外空间
        #方案二 将所有在前面的偶数和所有在后面的奇数对换
        x=0
        y=len(nums)-1
        while x<y:
            if nums[x]%2!=0:
                x+=1
                continue
            if nums[y]%2!=1:
                y-=1
                continue
            temp=nums[x]
            nums[x]=nums[y]
            nums[y]=temp
            x+=1
            y-=1
        return nums

s=Solution()
result= s.partitionArray([1, 2, 3, 4])
print(type(result))
print(result)
