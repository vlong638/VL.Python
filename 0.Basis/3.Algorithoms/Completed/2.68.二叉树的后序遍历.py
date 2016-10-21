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

    def postorderTraversal(self, root):
        # write your code here
        if root==None:
            return []
        #node
        result=[]
        self.postorderTraversalWithResult(root,result)
        return result
    def postorderTraversalWithResult(self, root,result):
        #left
        if root.left!=None:
            result.extend(self.postorderTraversal(root.left))
        #right
        if root.right!=None:
            result.extend(self.postorderTraversal(root.right))
        #node
        print("result.append",root.val)
        result.append(root.val)
        return result



A=TreeNode(0,TreeNode(1,TreeNode(11),TreeNode(12)),TreeNode(2,TreeNode(21),TreeNode(22)))
#     0
#  1      2
#11 12  21 22  
s=Solution()
result= s.postorderTraversal(A)
print(type(result))
print(result)
