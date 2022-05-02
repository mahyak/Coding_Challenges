# l1: 48 : 8 -> 4
# l2: 952: 2 -> 5 -> 9

# l3: 48 + 952 = 1000: 0 -> 0-> 0-> 1
# carry = 0
# l3: store the result 
# while l1 or l2 or carry:
#     x = if l1 is not empty -> x = l1.val else x = 0 
#     y = if l2 is not empy -> y = l2.val else y = 0
    
#     result = x+y+carry # 8+2+0 = 10
#     l3.val = result % 10 # 0
#     carry = result / 10 # 1
    
#     l2 = l2.next
#     l1 = l1.next
#     l3 = l3.next
    


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
    
#l1: 8 -> 4
#l2: 2 -> 5 -> 9
#l3: 0 -> 0 -> 0 -> 1->none

# step1: carry = 0, x=8, y=2; resul=10; 
# step2: carry = 1, x=4, y=5; result=10;
# step3: carry = 1, x=0, y=9; result=10;
# step4: carry = 1, x=0, y=0; result=1
