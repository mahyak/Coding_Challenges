```
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
```
 

Example 1:
```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```
Example 2:
```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

Solution
========
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        len_nums = len(nums)
        nums = sorted(nums)
        four_sum = []
        
        for i in range(len_nums):
            if i+1 < len_nums:
                three_sum = self.threeSum(nums[i+1:], target-nums[i])
                
                if three_sum:
                    for element in three_sum:
                        element.append(nums[i])
                        if element not in four_sum:
                            four_sum.append(element)
                        
        
        return four_sum
                    
    def threeSum(self, nums, target):
        three_sum = []
        
        for i in range(len(nums)):
            if i+1 < len(nums):
                two_sum = self.twoSum(nums[i+1:], target - nums[i])
                
                if two_sum:
                    for element in two_sum:
                        element.append(nums[i])
                        three_sum.append(element)
                            
        
        return three_sum
    
    def twoSum(self, nums, target):
        two_sum = []
        l = 0
        r = len(nums) - 1
        
        while l < r:
            if nums[l] + nums[r] == target:
                two_sum.append([nums[l], nums[r]])
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        
        return two_sum
```
