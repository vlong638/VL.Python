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
    @return: Preorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        if root==None:
            return []
        #node
        result=[]
        self.inorderTraversalWithResult(root,result)
        return result
    def inorderTraversalWithResult(self, root,result):
        #left
        if root.left!=None:
            result.extend(self.inorderTraversal(root.left))
        #node
        print("result.append",root.val)
        result.append(root.val)
        #right
        if root.right!=None:
            result.extend(self.inorderTraversal(root.right))
        return result



A=TreeNode(0,TreeNode(1,TreeNode(11),TreeNode(12)),TreeNode(2,TreeNode(21),TreeNode(22)))
#     0
#  1      2
#11 12  21 22  
s=Solution()
result= s.inorderTraversal(A)
print(type(result))
print(result)
