from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqrt = []
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if (nums[l] * nums[l]) < (nums[r] * nums[r]):
                sqrt.append(nums[r] * nums[r])
                r -= 1
            else:
                sqrt.append(nums[l] * nums[l])
                l += 1
        
        return list(reversed(sqrt))
            
                
# T: O(n)
# S: O(n)