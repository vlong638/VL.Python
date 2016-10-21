"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
#给定一个排序链表，删除所有重复的元素每个元素只留下一个。
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        #构建一个数组
        #构建一个删除数组内容一样删除链表第N个数的方法
        #然后然后对数组作消重处理
        #或者就像数组消重一样相似处理
        #本题略





        
s=Solution()
result= s.rotateString("abcd123456789",2)
print(type(result))
print(result)
