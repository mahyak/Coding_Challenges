class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}

        while head:
            if head.val in dic:
                dic[head.val] = 1 + dic[head.val]
            else:
                dic[head.val] = 1
            head = head.next

        node = ListNode()
        head = node

        for key, value in dic.items():
            if value == 1:
                new_node = ListNode(key)
                node.next = new_node
                node = new_node

        return head.next