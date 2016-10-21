"""
Definition of TreeNode:

        有两个不同大小的二进制树： T1 有上百万的节点； T2 有好几百的节点。
        请设计一种算法，判定 T2 是否为 T1的子树。
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if T1==None:
            return False
        if T1.val==T2.val:
            result= self.isSame(T1,T2)
            if result:
                print("isSame(T1,T2)",result)
                return True
        if T1.left!=None and T1.right!=None:
            return self.isSubtree(T1.left,T2) or self.isSubtree(T1.right,T2)
        elif T1.left!=None:
            return self.isSubtree(T1.left,T2)
        elif T1.right!=None:
            return self.isSubtree(T1.right,T2)
        else:
            return False
        

    def isSame(self,T1, T2):
        if T1==None and T2==None:
            return True
        else:
            return False
        if T1.val==T2.val:
            print(T1.val,T2.val)
            if T2.left==None and T2.right==None:
                return True
            else:
                left=self.isSame(T1.left,T2.left)
                right=self.isSame(T1.right,T2.right)
                return left and right
        return False
        


import Displayer
dis=Displayer.Displayer()
dis.DisplayTree(dis.SampleTree)
print()
from Displayer import TreeNode
s=Solution()

result= s.isSubtree(dis.SampleTree,TreeNode(2,TreeNode(21)))
print(type(result))
print(result)


result= s.isSubtree(dis.SampleTree,TreeNode(2,TreeNode(21),TreeNode(22)))
print(type(result))
print(result)

"""
result= s.isSubtree(dis.SampleTree,TreeNode(2,TreeNode(21),TreeNode(22)))
print(type(result))
print(result)
"""
