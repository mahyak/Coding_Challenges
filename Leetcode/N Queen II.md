
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

### Example 1:
```

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
```
### Example 2:
```
Input: n = 1
Output: 1
```

Solution 
========
``` python
class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negDiag = set() # (r - c)
        posDiag = set() # (r + c)
        
        res = []
        board = [["."] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = [".".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                col.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                board[r][c] = '.'
            
        backtrack(0)
     
        return len(res)
````
