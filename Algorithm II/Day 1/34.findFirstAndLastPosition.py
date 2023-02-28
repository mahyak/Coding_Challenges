from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = last = -1
        l, r = 0, len(nums)

        while l < r:
            mid = (r + l) // 2
            if nums[mid] == target:
                position = mid
                while position >= 0 and nums[position] == target:
                    first = position
                    position -= 1
                while mid < len(nums) and nums[mid] == target:
                    last = mid
                    mid += 1
                return [first, last]
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return [first, last]


# T: O(logn)
# S: O(1)