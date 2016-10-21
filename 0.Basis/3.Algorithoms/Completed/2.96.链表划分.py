"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
#给定一个单链表和数值x
#划分链表使得所有小于x的节点排在大于等于x的节点之前
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        if head==None:
            return None
        result=None
        current=None
        smallerHead=head
        while smallerHead!=None:
            if smallerHead.val<x:
                if current==None:
                    result=ListNode(smallerHead.val)
                    current=result
                    print("current",current.val)
                else:
                    current.next=ListNode(smallerHead.val)
                    print("current:",current.val,",next:",current.next.val)
                    current=current.next
            smallerHead=smallerHead.next
        greaterHead=head
        while greaterHead!=None:
            if greaterHead.val>=x:
                if current==None:
                    result=ListNode(greaterHead.val)
                    current=result
                    print("current",current.val)
                else:
                    current.next=ListNode(greaterHead.val)
                    print("current:",current.val,",next:",current.next.val)
                    current=current.next
            greaterHead=greaterHead.next
        return result
                
        
        

#1->4->3->2->5->2->null
a=ListNode(1,ListNode(4,ListNode(3,ListNode(2,ListNode(5,ListNode(2))))))
A=a
print("A:")
while A!=None:
    print(A.val)
    A=A.next
print()
s=Solution()
result= s.partition(a,3)
print("result:")
while result!=None:
    print(result.val)
    result=result.next
