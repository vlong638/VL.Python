"""
检查两棵二叉树是否等价。等价的意思是说，
首先两棵二叉树必须拥有相同的结构，
并且每个对应位置上的节点上的数都相等。
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, T1, T2):
        # Write your code here
        #判断当前节点是否相同
        #相同时,如果有下级节点,则进一步判断下级节点
        if T1==None and T2==None:
            return True
        elif T1==None or T2==None:
            return False
        else:
            if T1.val==T2.val:
                return self.isSame(T1.left,T2.left) and self.isSame(T1.right,T2.right)
            else:
                return False
