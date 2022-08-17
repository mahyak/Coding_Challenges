```
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
```
 

Example 1:
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
Example 2:
```
Input: nums = [1], k = 1
Output: [1]
```

Solution
========
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        sorted_dic = sorted(dic, key=dic.get, reverse=True)
        return sorted_dic[:k]
```        
