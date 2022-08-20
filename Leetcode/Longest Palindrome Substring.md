```
Given a string s, return the longest palindromic substring in s.
```
 

Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```
Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

Solution
========
```python
# O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            
            res, resLen = self.checkPalindrome(s, l, r, res, resLen)
            
            #even length
            l, r = i, i+1
            res, resLen = self.checkPalindrome(s, l, r, res, resLen)
            
        return res
    
    def checkPalindrome(self, s, l, r, res, resLen):
        while l >= 0 and r <len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l: r+1]
                resLen = r - l + 1
            
            l -= 1
            r += 1
            
        return res, resLen
```
