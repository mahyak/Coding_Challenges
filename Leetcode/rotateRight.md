```
Given the head of a linked list, rotate the list to the right by k places.
```
 

Example 1:
```

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```
Example 2:
```

Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

Solution
========
```python
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
```
