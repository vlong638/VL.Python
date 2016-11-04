"""
Definition of ListNode
"""
class ListNode(object):
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if head==None or head.next==None:
            return head
        if head.next.next==None:
            print("only two node, reverse it")
            next=head.next
            head.next=None
            next.next=head
            return next
        else:
            current=head.next
            next=head.next.next
            current.next=head
            head.next=None
            print("link {} to {}".format(current.val,head.val))
            print("link {} to {}".format(head.val,"None"))
            print("current:{} next:{}".format(current.val,next.val))
        while next.next!=None:
            temp=next.next
            next.next=current
            print("link {} to {}".format(next.val,current.val))
            current=next
            next=temp
            print("current:{} next:{}".format(current.val,next.val))
        next.next=current
        print("link {} to {}".format(next.val,current.val))
        print("current:{} next:{}".format(current.val,next.val))
        print("return next")
        return next
        
    def display(self, head):
        print("--start--")
        current=head
        while current!=None:
            print(current.val)
            current=current.next
        print("--end--")


head=ListNode(11,ListNode(222,ListNode(333,ListNode(4444,ListNode(555)))))
s=Solution()
s.display(head)
result= s.reverse(head)
s.display(result)

head=ListNode(11,ListNode(222))
s=Solution()
s.display(head)
result= s.reverse(head)
s.display(result)
