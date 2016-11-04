"""
Definition of ListNode
给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        # write your code here
        SampleListNode=ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
        current=SampleListNode
        while current.next.next!=None:
            if current.next.val==node.val:
                current.next=current.next.next
            else:
                current=current.next
        return SampleListNode

nodes=ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
import Displayer
dis=Displayer.Displayer()
dis.DisplayListNode(nodes)

s=Solution()
result= s.deleteNode(ListNode(3))
dis.DisplayListNode(result)
