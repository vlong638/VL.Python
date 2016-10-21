"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left, self.right = left, right
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if node==None:
            return root
        if root==None:
            return node
        current=root
        self.insertNodeRecursion(current,node)
        return root
    
    def insertNodeRecursion(self, root, node):
        if node.val>root.val:
            if root.right==None:
                root.right=node
            else:
                self.insertNodeRecursion(root.right,node)
        else:
            if root.left==None:
                root.left=node
            else:
                self.insertNodeRecursion(root.left,node)
                
    def preorderTraversal(self, root):
        # write your code here
        if root==None:
            return []
        #node
        result=[]
        self.preorderTraversalWithResult(root,result)
        return result
    
    def preorderTraversalWithResult(self, root,result):
        #node
        print("result.append",root.val)
        print("result:",result)
        result.append(root.val)
        #left
        if root.left!=None:
            result.extend(self.preorderTraversal(root.left))
        #right
        if root.right!=None:
            result.extend(self.preorderTraversal(root.right))
        return result
        

A=TreeNode(7,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(22,TreeNode(21),TreeNode(32)))
#     7
#  2      22
#1   3  21  32  
s=Solution()
result= s.insertNode(A,TreeNode(23))
print(s.preorderTraversal(result))
