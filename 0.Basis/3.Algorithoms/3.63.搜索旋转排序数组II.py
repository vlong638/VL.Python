"""
跟进“搜索旋转排序数组”，假如有重复元素又将如何？

是否会影响运行时间复杂度？

如何影响？

为何会影响？

写出一个函数判断给定的目标值是否出现在数组中。
"""
class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        i=0
        while i<len(A) and A[i]>target:
            i+=1
        while i<len(A):
            if A[i]==target:
                return True
            if A[i]>target:
                break
            i+=1
        return False


        
        
s=Solution()
result= s.search([3,4,4,5,7,0,1,2],2)
print(result)
