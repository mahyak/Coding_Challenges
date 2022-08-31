Find All Anagrams in a String (Leetcode #438)
===============================
### Medium

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

### Example 1:
Input:
`s: "cbaebabacd" p: "abc"`

Output:
`[0, 6]`

Explanation:

The substring with start index = 0 is "cba", which is an anagram of "abc".

The substring with start index = 6 is "bac", which is an anagram of "abc".

### Example 2:
Input:
`s: "abab" p: "ab"`

Output:
`[0, 1, 2]`

Explanation:

The substring with start index = 0 is "ab", which is an anagram of "ab".

The substring with start index = 1 is "ba", which is an anagram of "ab".

The substring with start index = 2 is "ab", which is an anagram of "ab".

Solution
========

```python
class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         p_len = len(p)
#         s_len = len(s)
#         if p_len == 0 or s_len == 0 or p_len > s_len:
#             return []
#         result = []
#         i = 0
#         p_sorted = sorted(p)
#         while i <= s_len-p_len:
#             if self.isAnagram(s[i:i+p_len], p_sorted):
#                 result.append(i)
#             i += 1
#         return result
    
#     def isAnagram(self, s, p):
#         return sorted(s) == p
  
# ===============================================#
# Another way of determining if they are anagram is to compare
# frequency of their letters
# Time Complexity: O(N)
  class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        pCount = {}
        sCount = {}
        
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            
        res = []
        
        if pCount == sCount:
            res.append(0)
        
        l = 0
        
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
            
        return res
```
tags: anagram, string
