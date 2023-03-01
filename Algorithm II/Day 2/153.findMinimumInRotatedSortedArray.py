from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        while nums[l] > nums[r]:
            mid = (r + l) // 2
            if nums[r] > nums[mid]:
                r = mid 
            else:
                l = mid + 1
        
        return nums[l]