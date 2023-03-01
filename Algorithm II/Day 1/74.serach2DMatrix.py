from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        column = len(matrix[0])
        left, right = 0, row * column - 1
        
        while left <= right: 
            mid = (left + right) // 2
            cur = matrix[mid // column][mid % column]
            if cur == target:
                return True
            elif cur > target:
                right = mid - 1
            else:
                left = mid + 1
        return False  
        
        