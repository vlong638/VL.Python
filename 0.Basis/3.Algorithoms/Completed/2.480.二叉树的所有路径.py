"""
给一棵二叉树，找出从根节点到叶子节点的所有路径
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        collection=[]
        if root==None:
            return collection
        if root.left==None and root.right==None:
            collection.append(str(root.val))
            return collection
        else:
            if root.left!=None:
                self.findLeaf(root.left,[str(root.val)],collection)
            if root.right!=None:
                self.findLeaf(root.right,[str(root.val)],collection)
        return collection

    def findLeaf(self,cur,prePath,pathCollection):
        #当前节点n,前置路径p,路径集合c
        #当n为叶子时,添加n到p,添加p到c
        #当n不为叶子时,
        
        prePath.append("->"+str(cur.val))
        if cur.left==None and cur.right==None:
            pathCollection.append("".join(prePath))
            return
        else:
            if cur.left!=None:
                self.findLeaf(cur.left,prePath[:],pathCollection)
            if cur.right!=None:
                self.findLeaf(cur.right,prePath[:],pathCollection)

from Displayer import Displayer,ListNode,TreeNode
dis=Displayer()
dis.DisplayTree(dis.SampleTree)

s=Solution()
result= s.binaryTreePaths(dis.SampleTree)
print(type(result))
print(result)

node= TreeNode(1,TreeNode(2,TreeNode(5),TreeNode(4)),TreeNode(3))
result= s.binaryTreePaths(node)
print(type(result))
print(result)

