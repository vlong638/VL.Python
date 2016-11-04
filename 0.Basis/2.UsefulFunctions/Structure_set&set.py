class Solution:
# @param s: a list of char
# @param offset: an integer 
# @return: nothing
    def intersection(self, nums1, nums2):
        set1=set(nums1)
        set2=set(nums2)
        result=set1&set2
        print("set1",set1)
        print("set2",set2)
        print("set1&set2",result)
        return list(result)


s=Solution()
result=s.intersection([1, 2, 2, 1],[2, 2])
print(result)
