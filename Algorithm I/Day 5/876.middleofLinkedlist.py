# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head 
        count = 0

        while node:
            count += 1
            node = node.next
        
        count = count // 2

        while count > 0:
            count -= 1
            head = head.next

        return head