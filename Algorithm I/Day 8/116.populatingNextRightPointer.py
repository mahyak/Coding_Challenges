"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
def bfs(q):
    length = len(q)
    
    if length == 0:
        return 
    
    while length > 0:
        node = q.pop(0)
        length -= 1
        if length != 0:
            node.next = q[0]
        if node.left:
            q.append(node.left)
            q.append(node.right)
    bfs(q)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        q = []
        q.append(root)
        bfs(q)

        return root
