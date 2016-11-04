"""
假设有一个排序的按未知的旋转轴旋转的数组
(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。
给定一个目标值进行搜索,
如果在数组中找到目标值返回数组中的索引位置，否则返回-1。

你可以假设数组中不存在重复的元素。
"""
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        i=0
        while i<len(A) and A[i]>target:
            i+=1
        while i<len(A):
            if A[i]==target:
                return i
            if A[i]>target:
                break
            i+=1
        return -1
s=Solution()
result= s.search([4, 5, 1, 2, 3],1)
print(result)
