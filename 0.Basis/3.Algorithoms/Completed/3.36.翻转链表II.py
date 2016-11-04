"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if m>=n:
            return head
        index=1
        startPre=None
        start=head
        while index!=m:
            startPre=start
            start=start.next
            if start==None:
                return None
            index+=1
        end=start
        endNext=end.next
        index=0
        while index!=n-m:
            #print(index,n-m,end.val)
            end=end.next
            endNext=end.next
            index+=1
        end.next=None
        newStart=self.reverse(start)
        newEnd=start
        newEnd.next=endNext
        #print("newEnd",newEnd.val)
        #print("endNext",endNext.val)
        #print("newStart",newStart.val)
        if startPre!=None:
            startPre.next=newStart
            #print("startPre",startPre.val)
        else:
            head=newStart
        return head
        
        
    def reverse(self, head):
        # write your code here
        if head==None or head.next==None:
            return head
        if head.next.next==None:
            #print("only two node, reverse it")
            next=head.next
            head.next=None
            next.next=head
            return next
        else:
            current=head.next
            next=head.next.next
            current.next=head
            head.next=None
            #print("link {} to {}".format(current.val,head.val))
            #print("link {} to {}".format(head.val,"None"))
            #print("current:{} next:{}".format(current.val,next.val))
        while next.next!=None:
            temp=next.next
            next.next=current
            #print("link {} to {}".format(next.val,current.val))
            current=next
            next=temp
            #print("current:{} next:{}".format(current.val,next.val))
        next.next=current
        #print("link {} to {}".format(next.val,current.val))
        #print("current:{} next:{}".format(current.val,next.val))
        #print("return next")
        return next


from Displayer import Displayer,ListNode,TreeNode
dis=Displayer()
dis.DisplayListNode(dis.SampleListNode)
s=Solution()
result=s.reverseBetween(dis.SampleListNode,1,2)
dis.DisplayListNode(result)
