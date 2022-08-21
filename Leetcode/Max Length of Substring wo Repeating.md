```
Given a string s, find the length of the longest substring without repeating characters.
```
### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
Solution
======

```python
# checking edge: if len(s) == 1 -> return 1
# two pointers -> left: l = 0, right: r = 1
# while r < len(s):
#   check if s[r] in s[l:r] -> r+=1, update the longestSub
#   else: iterate through s since s[r] in s[l:r] -> l+=1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        longestS = 0
        l = 0
        r = 1
        
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                longestS = max(longestS, len(s[l:r]))
            else:
                while s[r] in s[l:r]:
                           l += 1
        return longestS
```
