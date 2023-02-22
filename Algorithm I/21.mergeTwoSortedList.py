# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        h3 = l3

        while l1 and l2:
            val = 0
            if l1.val <= l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            node = ListNode(val)
            l3.next = node
            l3 = node
        
        if not l2:
            l3.next = l1
        if not l1:
            l3.next = l2

        return h3.next

# T: O(n+m)
# S: O(n+m)           
