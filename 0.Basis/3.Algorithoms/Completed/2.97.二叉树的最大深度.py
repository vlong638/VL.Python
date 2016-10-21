"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left, self.right = left, right
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def maxDepth(self, root):
        # write your code here
        if root==None:
            return 0
        return self.getDeep(root,0)
        

    def getDeep(self,root,deep):
        if root==None:
            return deep
        else:
            return max(self.getDeep(root.left,deep+1),self.getDeep(root.right,deep+1))
        

    

A=TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
#     3
#  9      20
#       15   7
B=TreeNode(3,None,TreeNode(20,TreeNode(15),TreeNode(7)))
#     3
#         20
#       15   7  

s=Solution()
result= s.maxDepth(A)
print(type(result))
print(result)
               
result= s.maxDepth(B)
print(type(result))
print(result)
