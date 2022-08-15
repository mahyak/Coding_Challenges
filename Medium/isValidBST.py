# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### BST Definition
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low = -math.inf, high = math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.left, low, node.val) and validate(node.right, node.val, high))
        return validate(root)
      
      
### INORDER          
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lst = self.inOrderTraverse(root)
        if lst == sorted(set(lst)):
            return True
        else:
            return False
        
    def inOrderTraverse(self, root):
        inorder = []
        
        if root:
            inorder = inorder + self.inOrderTraverse(root.left)
            inorder.append(root.val)
            inorder = inorder + self.inOrderTraverse(root.right)
        return inorder
