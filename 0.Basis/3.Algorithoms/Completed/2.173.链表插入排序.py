"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
#用插入排序对链表排序
class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        if head==None:
            return None
        newHead=head
        print("newHead ",newHead.val)
        current=head.next
        newHead.next=None
        while current!=None:
            temp=current
            current=current.next
            temp.next=None
            print("insert ",temp.val)
            newHead=self.insertionSort(newHead,temp)
            self.displayLinkList(newHead)
        return newHead   

    def insertionSort(self,head,node):
        #一个节点
        if head.next==None:
            if head.val>node.val:
                current=node
                node.next=head
                return node
            else:
                head.next=node
                return head
        current=head
        #大等于两个节点
        while current.next!=None:
            if current.val>node.val:
                node.next=current
                return node
            elif current.val<=node.val and current.next.val>node.val:
                temp=current.next
                current.next=node
                node.next=temp
                return head
            current=current.next
        #两个节点
        current.next=node
        return head
    
    def displayLinkList(self,result):
        print(result.val,end="->")
        while result!=None:
            if result.next==None:
                print("None")
            else:
                print(result.next.val,end="->")
            result=result.next

        

s=Solution()
head=ListNode(11111,ListNode(222,ListNode(333,ListNode(4444,ListNode(555)))))  
result= s.insertionSortList(head)
s.displayLinkList(result)

head=ListNode(3,ListNode(4,ListNode(1)))  
result= s.insertionSortList(head)
s.displayLinkList(result)
