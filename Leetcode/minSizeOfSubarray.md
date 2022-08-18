```
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
```
 

Example 1:
```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```
Example 2:
```
Input: target = 4, nums = [1,4,4]
Output: 1
```
Example 3:
```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

Solution
========
```python
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
```
