
```
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
```
 

Example 1:
```

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```
Example 2:
```
Input: l1 = [0], l2 = [0]
Output: [0]
```
Example 3:
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```
Solution
========
```
l1: 48 : 8 -> 4
l2: 952: 2 -> 5 -> 9

l3: 48 + 952 = 1000: 0 -> 0-> 0-> 1
carry = 0
l3: store the result 
while l1 or l2 or carry:
    x = if l1 is not empty -> x = l1.val else x = 0 
     y = if l2 is not empy -> y = l2.val else y = 0
    
     result = x+y+carry # 8+2+0 = 10
     l3.val = result % 10 # 0
     carry = result / 10 # 1
    
     l2 = l2.next
     l1 = l1.next
     l3 = l3.next 
```
    
```python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        head3 = l3
        carry = 0
        
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            result = x + y + carry
            l3.next = ListNode(result%10)
            carry = int(result/10)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3 = l3.next
            
        return head3.next
```
