class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length = 1
        
        while k > 0 and head and head.next:
            node = head
            prev = None
            
            while node.next:
                prev = node
                node = node.next  
                length += 1
            
            if k > length:
                k = (k%length)
            
            if k > 0:
                node.next = head
                prev.next = None
                head = node
           
            k -= 1
            
        return head
