class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev_node = None
        stack = []
        stack.append(head)
        
        if not head:
            return None
        
        while stack:
            curr = stack.pop()
            
            if prev_node:
                curr.prev = prev_node
                prev_node.next = curr
            
            prev_node = curr
            
            if curr.next:
                stack.append(curr.next)
                
            if curr.child:
                stack.append(curr.child)
                curr.child = None
        
        return head
