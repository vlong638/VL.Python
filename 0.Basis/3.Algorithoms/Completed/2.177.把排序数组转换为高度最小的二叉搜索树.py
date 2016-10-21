"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        length=len(A)
        if length==0:
            return None
        medium=int(length/2)
        leftRange=[]
        index=0
        while index<medium:
            leftRange.append(A.pop(0))
            index+=1        
        root=TreeNode(A.pop(0))
        rightRange=A
        if len(leftRange)>0:
            self.buildTree(root,1,leftRange)
        if len(rightRange)>0:
            self.buildTree(root,2,rightRange)
        return root

    def buildTree(self,parent,side,array):
        print("side",side,"buid",array)
        length=len(array)
        if length==1:
            if side==1:
                parent.left=TreeNode(array[0])

            else:
                parent.right=TreeNode(array[0])
        else:
            medium=int(length/2)
            leftRange=[]
            index=0
            while index<medium:
                leftRange.append(array.pop(0))
                index+=1
            mediumNode=TreeNode(array.pop(0))
            rightRange=array
            if side==1:
                parent.left=mediumNode

            else:
                parent.right=mediumNode
            if len(leftRange)>0:
                self.buildTree(mediumNode,1,leftRange)
            if len(rightRange)>0:
                self.buildTree(mediumNode,2,rightRange)

            
        

import Displayer
s=Solution()
result=s.sortedArrayToBST([1,2,3,4,5,6,7])
dis=Displayer.Displayer()
dis.DisplayTree(result)
print()
result=s.sortedArrayToBST([0])
dis=Displayer.Displayer()
dis.DisplayTree(result)
print()
result=s.sortedArrayToBST([-1,0,1,3])
dis=Displayer.Displayer()
dis.DisplayTree(result)

"""
关于树的处理辅助
import Displayer
dis=Displayer.Displayer()
dis.DisplayTree(dis.SampleTree)
"""
