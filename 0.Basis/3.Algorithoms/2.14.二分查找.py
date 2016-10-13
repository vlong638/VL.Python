class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        start=0
        end=len(nums)-1
        return self.binarySearchWithRange(nums,target,start,end)
            
    def binarySearchWithRange(self, nums, target,start,end):
        print("check range{}-{}".format(start,end))
        # write your code here
        index=int((start+end)/2)
        if nums[index]==target:
            print("find it,at index:",index)
            while index>1 and nums[index-1]==target:
                print("move forward")
                index-=1
            print("return",index)
            return index
        elif nums[index]>target:
            if index-1<start:
                print("reach boundary,start:{},index:{}".format(index,start))
                return -1;
            print("less than medium:{}".format(nums[index]))
            return self.binarySearchWithRange(nums,target,start,index-1)
        else:
            if index+1>end:
                print("reach boundary,index:{},end:{}".format(index,end))
                return -1;
            print("great than medium:{}".format(nums[index]))
            return self.binarySearchWithRange(nums,target,index+1,end)
            
            
        
s=Solution()
result= s.binarySearch([1,4,4,5,7,7,8,9,9,10],1)
print(type(result))
print(result)
