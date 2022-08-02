class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == root.val or q.val == root.val:
            return root
        if p.val > root.val:
            if q.val < root.val:
                return root
            else:
                return self.lowestCommonAncestor(root.right, p, q)
        if q.val > root.val:
            return root
        else:
            return self.lowestCommonAncestor(root.left, p, q)
