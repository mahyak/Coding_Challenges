class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            head.val, head.next.val = head.next.val, head.val
            if head.next.next:
                self.swapPairs(head.next.next)
        return head
