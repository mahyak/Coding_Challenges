# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        prev = head
        curr = head.next
        prev.next = None
        
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
        
        
