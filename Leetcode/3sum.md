3Sum (Leetcode #15)
===============================
### Medium
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
Notice that the solution set must not contain duplicate triplets.
### Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```
### Example 2:
```
Input: nums = []
Output: []
```
### Example 3:
```
Input: nums = [0]
Output: []
```

Solution
========
```
# For each element in the list check -> if the 
# target = -element is equal to  sum of two other 
# elements after the the element's index. improve
# twoSum by soting the list and remove the same values 
# mean using set(). compare twoSum result with target, 
# if twoSum>target end -= 1, if twoSum<target -> 
# start += 1, else: add to the final result.
```
```python
# T: O(NlogN + N^2)
# S: O(N) or O(NlogN) based on sort()
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = set()
        
        for index in range(len(nums)):
            target = -sorted_nums[index]
            start = index + 1
            end = len(nums) - 1
            
            while start < end:
                two_sum = sorted_nums[start] + sorted_nums[end]
                if two_sum < target: 
                    start += 1
                elif two_sum > target:
                    end -= 1
                else:
                    result.add((-target, sorted_nums[start], sorted_nums[end]))
                    start += 1
                    end -= 1
        return result
            
```
