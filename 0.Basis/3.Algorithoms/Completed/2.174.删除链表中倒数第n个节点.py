"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        current,length=self.nthToLast(head,n+1)
        print("n",n,"length",length)
        if n==length:
            return head.next
        elif n>length:
            return head
        else:
            current.next=current.next.next
            return head
        
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
        return current,length
        
    def displayLinkList(self,result):
        if result==None:
            print("None")
        print(result.val,end="->")
        while result!=None:
            if result.next==None:
                print("None")
            else:
                print(result.next.val,end="->")
            result=result.next

head=ListNode(11,ListNode(222,ListNode(333,ListNode(4444,ListNode(555)))))
s=Solution()
s.displayLinkList(head)
resultNode= s.removeNthFromEnd(head,5)
s.displayLinkList(resultNode)

head=ListNode(11)
s.displayLinkList(head)
resultNode= s.removeNthFromEnd(head,1)
s.displayLinkList(resultNode)
