"""
给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。

如果目标值不在数组中，则返回[-1, -1]
"""
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        i=0
        while i < len(A):
            if A[i]==target:
                start=i
                while i<len(A)-1 and A[i+1]==target:
                    i+=1
                end=i
                return [start,end]
            i+=1
        return [-1,-1]
        
s=Solution()
result= s.searchRange([5, 7, 7, 8, 8, 10],7)
print(result)
