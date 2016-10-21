"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

找到单链表倒数第n个节点，保证链表中节点的最少数量为n。
"""
class ListNode(object):
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
import gc  
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        if head==None:
            return None
        current=head
        length=0
        while current!=None:
            length+=1
            current=current.next
        current=head
        currentIndex=0
        while currentIndex<length-n:
            current=current.next
            currentIndex+=1
        return current

    
    """
    #使用动态规划的方式处理,空间消耗较高
    #引入了gc和gc.collect()手动清理内容则会降低效率
    def nthToLast(self, head, n):
        # write your code here
        node,length=self.findNthToLastIndex(head,n)
        return node

    def findNthToLastIndex(self,head,n) :
        if head.next==None:
            if n==1:
                return head,1
            else:
                return None,1
        else:
            node,index=self.findNthToLastIndex(head.next,n)
            index+=1
            if node!=None:
                return node,index
            elif index==n:
                return head,index
            else:
                return None,index
    """

        
        

head=ListNode(11,ListNode(222,ListNode(333,ListNode(4444,ListNode(555)))))
s=Solution()
resultNode= s.nthToLast(head,1)
print(resultNode.val)
resultNode= s.nthToLast(head,2)
print(resultNode.val)
resultNode= s.nthToLast(head,3)
print(resultNode.val)
resultNode= s.nthToLast(head,4)
print(resultNode.val)
resultNode= s.nthToLast(head,5)
print(resultNode.val)

