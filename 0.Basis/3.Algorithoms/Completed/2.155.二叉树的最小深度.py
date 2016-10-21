"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    给定一个二叉树，找出其最小深度。
    二叉树的最小深度为根节点到最近叶子节点的距离。
         1

         /     \ 

       2       3

              /    \

            4      5  

    这个二叉树的最小深度为 2
    """ 
    def minDepth(self, root):
        # write your code here
        if root==None:
            return 0
        return self.getMinDeep(root,1)        

    def getMinDeep(self,root,deep):
        if root.left==None and root.right==None:
            return deep
        elif root.left==None:
            return self.getMinDeep(root.right,deep+1)
        elif root.right==None:
            return self.getMinDeep(root.left,deep+1)
        else:
            return min(self.getMinDeep(root.left,deep+1),self.getMinDeep(root.right,deep+1))
    

A=TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
#     3
#  9      20
#       15   7
B=TreeNode(3,None,TreeNode(20,TreeNode(15),TreeNode(7)))
#     3
#         20
#       15   7  

s=Solution()
result= s.minDepth(A)
print(type(result))
print(result)
result= s.minDepth(B)
print(type(result))
print(result)
