```
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
```

Solution
========
```python

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
 ```     
 ```python     
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
```
