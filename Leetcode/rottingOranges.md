
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:
```

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```
Example 2:

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```
Example 3:
```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

Solution 
========
```python
def dfs(grid, i, j, counter, start):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or (grid[i][j] < 0 and -grid[i][j] < counter):
        return
    
    if start is False and grid[i][j] == 2:
        return 

    grid[i][j] = -counter
    up = dfs(grid, i-1, j, counter+1,  False)
    down = dfs(grid, i+1, j, counter+1,  False)
    left = dfs(grid, i, j-1, counter+1,  False)
    right = dfs(grid, i, j+1, counter+1,  False)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_ = 0
    

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    dfs(grid, row, col, 0, True)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
                max_ = max(abs(grid[row][col]), max_)

        return max_
                    

```
