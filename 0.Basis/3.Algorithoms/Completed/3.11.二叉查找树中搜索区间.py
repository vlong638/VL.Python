"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        result=[]
        self.searchRangeWithResult(root,k1,k2,result)
        result.sort()
        return result

    def searchRangeWithResult(self, root, k1, k2, result):
        # write your code here
        if root==None:
            return
        if root.val>=k1 and root.val<=k2:
            result.append(root.val)
            self.searchRangeWithResult(root.left,k1,k2,result)
            self.searchRangeWithResult(root.right,k1,k2,result)
        elif root.val<k1:
            self.searchRangeWithResult(root.right,k1,k2,result)
        else:
            self.searchRangeWithResult(root.left,k1,k2,result)
        

from Displayer import Displayer,ListNode,TreeNode
dis=Displayer()
dis.DisplayTree(dis.SampleTree3)


s=Solution()
result= s.searchRange(dis.SampleTree3,0,15)
print(type(result))
print(result)
