from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] == 0:
                del nums[l]
                nums.append(0)
                r -= 1
            else: 
                l += 1





# T: O(n)
# S: O(1)
