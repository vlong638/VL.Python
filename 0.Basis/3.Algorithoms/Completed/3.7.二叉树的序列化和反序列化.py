"""
设计一个算法，并编写代码来序列化和反序列化二叉树。
将树写入一个文件被称为“序列化”，
读取文件后重建同样的二叉树被称为“反序列化”。

如何反序列化或序列化二叉树是没有限制的，
你只需要确保可以将二叉树序列化为一个字符串，
并且可以将字符串反序列化为原来的树结构。
"""
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self,root):
        # write your code here
        result=[]
        self.preorderTraversalWithResult(root,result)
        return result
    
    def preorderTraversalWithResult(self,root,result):
        if root!=None:
            result.append(root.val)
            self.preorderTraversalWithResult(root.left,result)
            self.preorderTraversalWithResult(root.right,result)
        else:
            result.append("#")

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        if len(data)==0:
            return None
        value=data.pop(0)
        if value=="#":
            return None
        else:
            root=TreeNode(value)
            self.preorderTraversalToBuildTree(root,data,0)
            self.preorderTraversalToBuildTree(root,data,1)
            return root
        
    def preorderTraversalToBuildTree(self,root,data,side):
        if len(data)==0:
            return
        
        value=data.pop(0)
        if value=="#":
            return
        else:
            if side==0:
                root.left=TreeNode(value)
                self.preorderTraversalToBuildTree(root.left,data,0)
                self.preorderTraversalToBuildTree(root.left,data,1)
            else:
                root.right=TreeNode(value)
                self.preorderTraversalToBuildTree(root.right,data,0)
                self.preorderTraversalToBuildTree(root.right,data,1)
                
            
            
    


from Displayer import Displayer,ListNode,TreeNode
dis=Displayer()
dis.DisplayTree(dis.SampleTree)
print()

s=Solution()
result= s.serialize(dis.SampleTree)
print(type(result))
print(result)

node= s.deserialize(result)
dis.DisplayTree(node)
