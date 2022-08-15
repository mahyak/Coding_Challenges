class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0]) - 1
        row = 0
        
        while cols >= 0 and row < rows:
            if target < matrix[row][cols]:
                cols -= 1
            elif target > matrix[row][cols]:
                row +=1
            else:
                return True
        return False
