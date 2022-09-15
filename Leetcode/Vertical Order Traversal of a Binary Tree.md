Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

###Example 1:
![img](https://assets.leetcode.com/uploads/2021/01/29/vtree1.jpg)
```
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
```

###Example 2:
![img2](https://assets.leetcode.com/uploads/2021/01/29/vtree2.jpg)
```
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
```

###Example 3:
![img3](https://assets.leetcode.com/uploads/2021/01/29/vtree3.jpg)
```
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
```

solution
======
```python
# BFS Traverse
# Store [node, row, col] in queue
# Store vertical position in dic: key = row, value: (col, node.val)
# Time Complexity: O(N)

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        vertical = defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node, x, y = queue.popleft()
                vertical[x].append((y, node.val))
                if node.left:
                    queue.append((node.left, x - 1, y + 1))
                if node.right:
                    queue.append((node.right, x + 1, y + 1))
        res = []
        for x in sorted(vertical.keys()):
            res.append([tup[1] for tup in sorted(vertical[x])])
        return res
  ```
