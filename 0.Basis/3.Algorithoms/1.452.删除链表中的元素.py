import PrintHelper
# Definition for singly-linked list.
PrintHelper.PrintCode('class ListNode:')
PrintHelper.PrintCode('    def __init__(self, x):')
PrintHelper.PrintCode('        self.val = x')
PrintHelper.PrintCode('        self.next = None')
PrintHelper.PrintCode('')
PrintHelper.PrintCode('class Solution:')
PrintHelper.PrintCode('    # @param head, a ListNode')
PrintHelper.PrintCode('    # @param val, an integer')
PrintHelper.PrintCode('    # @return a ListNode')
PrintHelper.PrintCode('    def removeElements(self, head, val):')
PrintHelper.PrintCode('        # Write your code here')
PrintHelper.PrintCode('        if head==None or head.next==None:')
PrintHelper.PrintCode('            return None        ')
PrintHelper.PrintCode('        current=head')
PrintHelper.PrintCode('        while current.next!=None and current.next.next!=None:')
PrintHelper.PrintCode('            if current.next.val==val:')
PrintHelper.PrintCode('                current.next=current.next.next')
PrintHelper.PrintCode('            current=current.next')
PrintHelper.PrintCode('        current=head')
PrintHelper.PrintCode('        if current.val==val:')
PrintHelper.PrintCode('            return head.next')
PrintHelper.PrintCode('        return head')
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if head==None or head.next==None:
            return None        
        current=head
        while current.next!=None and current.next.next!=None:
            if current.next.val==val:
                current.next=current.next.next
            current=current.next
        current=head
        if current.val==val:
            return head.next
        return head
PrintHelper.PrintCode('a=ListNode(101)')
a=ListNode(101)
PrintHelper.PrintCode('a.next=(ListNode(102))')
a.next=(ListNode(102))
PrintHelper.PrintCode('a.next.next=(ListNode(103))')
a.next.next=(ListNode(103))
PrintHelper.PrintCode('solution=Solution()')
solution=Solution()
PrintHelper.PrintCode('b=a')
b=a
PrintHelper.PrintCode('while b!=None:')
PrintHelper.PrintCode('    print(b.val)')
PrintHelper.PrintCode('    b=b.next')
PrintHelper.PrintCode('print()')
while b!=None:
    print(b.val)
    b=b.next
print()
PrintHelper.PrintCode('c= solution.removeElements(a,101)')
PrintHelper.PrintCode('while c!=None:')
PrintHelper.PrintCode('    print(c.val)')
PrintHelper.PrintCode('    c=c.next')
c= solution.removeElements(a,101)
while c!=None:
    print(c.val)
    c=c.next



