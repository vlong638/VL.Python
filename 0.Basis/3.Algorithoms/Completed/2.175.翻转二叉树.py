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
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        temp=root.left
        root.left=root.right
        root.right=temp
        if root.left!=None:
            self.invertBinaryTree(root.left)
        if root.right!=None:
            self.invertBinaryTree(root.right)
        return root
        
    
import Displayer

A=TreeNode(0,TreeNode(1,TreeNode(11,TreeNode(0),TreeNode(23)),TreeNode(12)),TreeNode(2,TreeNode(21),TreeNode(22)))
#        0  
#    1        2 
#11    12  21     22


dis=Displayer.Displayer()
dis.DisplayTree(A)
print()
s=Solution()
result= s.invertBinaryTree(A)
dis.DisplayTree(result)
"""
"""
