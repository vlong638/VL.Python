class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, nums, target):
        # write your code here
        if nums==None or len(nums)==0:
            nums=[target]
            return nums
        start=0
        end=len(nums)-1
        index=self.binarySearchWithRange(nums,target,start,end)
        nums.insert(index,target)
        return index
            
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
            if index==start:
                print("reach boundary,start:{},index:{}".format(index,start))
                return index;
            print("less than medium:{}".format(nums[index]))
            return self.binarySearchWithRange(nums,target,start,index-1)
        else:
            if index==end:
                print("reach boundary,index:{},end:{}".format(index,end))
                return index+1;
            print("great than medium:{}".format(nums[index]))
            return self.binarySearchWithRange(nums,target,index+1,end)


        
s=Solution()
result= s.searchInsert([],0)
print(type(result))
print(result)
