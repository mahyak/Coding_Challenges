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
                    
                    
                
        

