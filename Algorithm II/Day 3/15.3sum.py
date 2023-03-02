from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = set()
        
        for i in range(len(nums)):
            target = -sorted_nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                two_sum = sorted_nums[l] + sorted_nums[r]
                if two_sum < target: 
                    l += 1
                elif two_sum > target:
                    r -= 1
                else:
                    result.add((-target, sorted_nums[l], sorted_nums[r]))
                    l += 1
                    r -= 1
        return result
            