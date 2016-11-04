class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        mapper={}
        for num in nums:
            numCount=mapper.get(num)
            if numCount:
                mapper[num]+=1
            else:
                mapper[num]=1
        print("len(nums):",len(nums))
        for num in mapper:
            if mapper[num] >len(nums)/3:
                print(str(num)+":",mapper[num])
                return num
            else:
                print(str(num)+":",mapper[num])
        return None


        
s=Solution()
result= s.majorityNumber([0,1,1,1,1,1,2,2,2])
print(type(result))
print(result)
