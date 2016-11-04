"""
给一个链表，两两交换其中的节点，然后返回交换后的链表。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # Write your code here
        if head==None or head.next==None:
            return head
        if  head!=None and head.next!=None:
            temp1=head
            temp2=head.next
            temp3=head.next.next
            #pre=temp2
            temp2.next=temp1
            temp1.next=temp3
            cur=temp3
            pre=temp1
        head=temp2
        while cur!=None and cur.next!=None:
            temp1=cur
            temp2=cur.next
            temp3=cur.next.next
            pre.next=temp2
            temp2.next=temp1
            temp1.next=temp3
            cur=temp3
            pre=temp1
        return head


from Displayer import Displayer,ListNode,TreeNode
dis=Displayer()
dis.DisplayListNode(dis.SampleListNode)
s=Solution()
result= s.swapPairs(dis.SampleListNode)
dis.DisplayListNode(result)
