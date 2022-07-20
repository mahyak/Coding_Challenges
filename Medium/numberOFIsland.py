class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      rows = len(grid)
      cols = len(grid[0])
      island = 0
      
      for row in range(rows):
        for col in range(cols):
          if grid[row][col] == '1':
            island += 1
            self.bfs(row, col, grid)
     
   def bfs(self, row, col, grid):
    row = len(grid)
    col = len(grid[0])
    
    if i<0 or j<0 or i>=rows or j>=cols or grid[i][j] != '1':
      return
    
    self.bfs(i+1, j)
    self.bfs(i-1, j)
    self.bfs(i, j+1)
    self.bfs(i, j-1)
