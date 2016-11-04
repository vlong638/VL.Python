"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    深度复制一个二叉树。

给定一个二叉树，返回一个他的 克隆品 。
    """
    def cloneTree(self, root):
        # Write your code here
        if root==None:
            return None

        clonedTree=TreeNode(root.val)
        self.cloneSubTree(root,clonedTree)
        return clonedTree
        
    def cloneSubTree(self, root,clonedTree):
        if root==None:
            return
        if root.left!=None:
            clonedTree.left=TreeNode(root.left.val)
            self.cloneSubTree(root.left,clonedTree.left)
        if root.right!=None:
            clonedTree.right=TreeNode(root.right.val)
            self.cloneSubTree(root.right,clonedTree.right)
        

from Displayer import Displayer,TreeNode
dis=Displayer()
dis.DisplayTree(dis.SampleTree)
s=Solution()
result= s.cloneTree(dis.SampleTree)
dis.DisplayTree(result)
