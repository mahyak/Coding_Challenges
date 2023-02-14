# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        count = 0

        while node:
            count += 1
            node = node.next

        if count == 1:
            return None
        
        if count == n:
            return head.next

        removed = head
        prev = head
        count = count-n
       
        while count > 0:
            count -= 1
            prev = removed
            removed = removed.next
   
        prev.next = removed.next   

        return head 
       
    
