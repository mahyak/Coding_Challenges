```
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
```
 

Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```
Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

Solution
========
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums) 
        right = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        
        for j in reversed(range(0, len(nums)-1)):
            right[j] = right[j+1] * nums[j+1]
        
        for i in range(len(nums)):
            nums[i] = right[i]*left[i]
        return nums
```
