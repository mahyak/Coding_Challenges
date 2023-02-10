from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        n = len(nums)
        k %= n
        j = 0
        
        while k > 0:
            for _ in range(k):
                nums[j], nums[n - k + j] = nums[n - k + j], nums[j]
                j += 1
            n -= k
            k %= n
        