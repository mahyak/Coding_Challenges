def dfs(grid, r, c, area):
    rows, cols = len(grid), len(grid[0])
    
    if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0):
        return 0
   
    grid[r][c] = 0
    dfs(grid, r+1, c, area +1)
    dfs(grid, r-1, c, area +1)
    dfs(grid, r, c+1, area +1)
    dfs(grid, r, c-1, area +1)
    
    return area

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    island_area = dfs(grid, r, c, area)
                    max_area = max(max_area, island_area)
        return max_area
