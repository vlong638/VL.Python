"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
将两个排序链表合并为一个新的排序链表
"""
class ListNode(object):
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        #将合并数组改为合并链表即可
        #略
        
    def mergeSortedArray(self, A, B):
        # write your code here
        c=[]
        a=None
        b=None
        while len(A)>0:
            if a==None:
                a=A.pop(0)
            if len(B)==0:
                c.append(a)
                print("append",a)
                c.extend(A)
                print("extend",A)
                break
            elif b==None:
                b=B.pop(0)
            print(a,b)
            if a>b:
                c.append(b)
                print("append",b)
                b=None
            else:
                c.append(a)
                print("append",a)
                a=None
        if a!=None:
            c.append(a)
            print("append",a)
        if b!=None:
            c.append(b)
            print("append",b)
        if len(B)>0:
            c.extend(B)
            print("extend",B)
        return c
    
headA=ListNode(11,ListNode(222,ListNode(333,ListNode(4444,ListNode(5556)))))
headB=ListNode(12,ListNode(212,ListNode(331,ListNode(4444,ListNode(5555)))))
s=Solution()
result= s.mergeTwoLists(headA,headB)
print(type(result))
print(result)
