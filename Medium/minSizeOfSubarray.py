class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float('inf')
        left, _sum = 0, 0
        
        for i in range(0, len(nums)):
            _sum += nums[i]
            
            while _sum >= target:
                min_size = min(min_size, i + 1 - left)
                _sum -= nums[left]
                left += 1
                
        return min_size if min_size != float('inf') else 0
