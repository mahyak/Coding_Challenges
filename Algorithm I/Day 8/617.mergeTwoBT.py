def bfs(q):
    length = len(q)

    if length == 0:
        return 

    while length > 0:
        node1 = q.pop(0)
        node2 = q.pop(0)
        node1.val = (node1.val + node2.val)

        if node1.left:
            if not node2.left:
                node2.left = TreeNode(val=0)
            q.append(node1.left)
            q.append(node2.left)
        else:
            if node2.left:
                node1.left = node2.left
                node2.left = TreeNode(val=0)
                q.append(node2.left)
                q.append(node1.left)

        if node1.right:
            if not node2.right:
                node2.right = TreeNode(val=0)
            q.append(node1.right)
            q.append(node2.right)
        else:
            if node2.right:
                node1.right = node2.right
                node2.right = TreeNode()
                q.append(node2.right)
                q.append(node1.right)
            
        length -= 2
            
    bfs(q)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        q = []
        q.append(root1)
        q.append(root2)
        
        bfs(q)
        
        return root1










# root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# q1 = [3, 2]
# q2 = [null, 4]
