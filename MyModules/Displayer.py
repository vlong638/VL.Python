"""
from Displayer import Displayer,ListNode,TreeNode
dis=Displayer()
dis.DisplayTree(dis.SampleTree)
dis.DisplayListNode(dis.SampleListNode)
"""

#链表节点
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
#树形节点     
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left, self.right = left, right
        
class Displayer:
    #1->2->3->4
    SampleListNode=ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
    #            0  
    #       1        2 
    #   11    12  21     22
    #0     23
    SampleTree=TreeNode(0,TreeNode(1,TreeNode(11,TreeNode(0),TreeNode(23)),TreeNode(12)),TreeNode(2,TreeNode(21),TreeNode(22)))
    #            98  
    #       97        NA
    #     NA   88  
    #        NA   84
    #           NA   79
    #             87     64
    #           NA  NA NA  63
    #                    69  62
    SampleTree2=TreeNode(98,TreeNode(97,None,TreeNode(88,None,TreeNode(84,None,TreeNode(79,TreeNode(87),TreeNode(64,None,TreeNode(63,TreeNode(69),TreeNode(62))))))))
    #            4  
    #       2        16 
    #    0     3  8     17
    #      1
    SampleTree3=TreeNode(4,TreeNode(2,TreeNode(0,None,TreeNode(1)),TreeNode(3)),TreeNode(16,TreeNode(8),TreeNode(17)))

    #ListNode
    def DisplayListNode(self,root):
        current=root
        while current!=None:
            print(current.val,end="->")
            current=current.next
        print("None")

    #Tree
    lx=6
    lw=4    
    wordPattern="{: ^"+str(lw)+"}"
    def DisplayTree(self,root):
        texts=[]
        deep=self.getMaxDeep(root,0)
        x=deep-1
        y=deep-1
        for xd in range(deep):
            texts.append("")
        self.climbTree(texts,root,x,y,deep,True)
        for text in texts:
            print(text)      
        
    def climbTree(self,texts,root,x,y,deep,isLeft):
        #添加行
        #print("x:",x,"y:",y)
        self.appendTreeLine(texts,root,x,y,deep,isLeft)
        if root!=None:
            #继续爬
            self.climbTree(texts,root.left,x-1,y-1,deep,True)
            self.climbTree(texts,root.right,x+1,y-1,deep,False)
            
    def appendTreeLine(self,texts,root,x,y,deep,isLeft):
        if x<0 or y<0:
            return
        elif root==None:
            #value="NA"
            value=""
        else:
            value=root.val
        preLength=int(self.getPre(y))
        pre=preLength*" "
        #print("pre",self.getPre(y))
        if y==0:
            intra=self.lx*"^"
            if isLeft:
                texts[deep-y-1]+=self.wordPattern.format(value)
            else:
                texts[deep-y-1]+=intra+self.wordPattern.format(value) 
        else:
            intra=2*preLength*"^"
            #texts[deep-y-1]+=pre+self.wordPattern.format(value)+pre
            if isLeft:
                texts[deep-y-1]+=pre+self.wordPattern.format(value)
            else:
                texts[deep-y-1]+=intra+self.wordPattern.format(value)+pre

    def getPre(self,y):
        if y<=0:
            return 1;
        elif y==1:
            return int(self.lw/2+self.lx/2)
        else:
            return self.getPre(y-1)*2+self.lw/2

  
    def getMaxDeep(self,root,deep):
        if root==None:
            return deep
        else:
            return max(self.getMaxDeep(root.left,deep+1),self.getMaxDeep(root.right,deep+1))
