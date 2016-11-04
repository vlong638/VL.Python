"""
将一棵二叉树按照前序遍历拆解成为一个假链表。所谓的假链表是说，用二叉树的 right 指针，来表示链表中的 next 指针。

 注意事项

不要忘记将左儿子标记为 null，否则你可能会得到空间溢出或是时间溢出。
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
import pdb
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if root==None:
            return root
        self.preorderTraversalWithResult(root)
        return root
        
    def preorderTraversalWithResult(self,cur):
        #返回
        if cur.left==None and cur.right==None:
            return cur,cur
        #整理左侧区间
        curRight=cur.right
        if cur.left!=None:
            leftStart,leftEnd=self.preorderTraversalWithResult(cur.left)
            leftEnd.right=cur.right
            cur.right=leftStart
            cur.left=None
        else:
            leftStart=cur
            leftEnd=cur
        #整理右侧区间
        if curRight!=None:
            rightStart,rightEnd=self.preorderTraversalWithResult(curRight)
        else:
            rightStart=cur
            rightEnd=cur
        #返回    
        self.display(cur)
        return cur,rightEnd
    
    def display(self,current):
        while current!=None:
            print("current.val",current.val)
            if current.left!=None:
                print("current.left.val",current.left.val)
            current=current.right
        print()

    
from Displayer import Displayer,ListNode,TreeNode
dis=Displayer()
dis.DisplayTree(dis.SampleTree)

s=Solution()
result= s.flatten(dis.SampleTree)

current=result
s.display(current)

dis.DisplayTree(dis.SampleTree2)

s=Solution()
result= s.flatten(dis.SampleTree2)

current=result
s.display(current)
#dis.DisplayTree(result)
