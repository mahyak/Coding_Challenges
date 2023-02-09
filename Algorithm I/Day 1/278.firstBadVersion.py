# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = (r + l) // 2
            if not isBadVersion(mid):
                l = mid + 1
            elif isBadVersion(mid-1):
                r = mid - 1
            else:
                return mid
     

# n = 5 [False, False, False, True, True]
# l = 3, r = 5 , mid = 4

# T: O(logn)
# S: O(1)
