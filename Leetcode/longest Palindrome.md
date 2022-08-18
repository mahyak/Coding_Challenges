```
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
```
 

Example 1:
```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
```
Example 2:
```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 ```
 
 Solution
 ========
 ```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        
        for i in range(len(s)):
            l, r = i, i
            res, resLen = self.checkPalidrome(s, l, r, res, resLen)
            
            l, r = i, i+1
            res, resLen = self.checkPalidrome(s, l, r, res, resLen)
        
        return res
    
    def checkPalidrome(self, s, l, r, res, resLen):
        while l>=0 and r<len(s) and s[l] == s[r]:
            if (r-l+1) > len(res):
                resLen = r-l+1
                res = s[l:r+1]
            r += 1
            l -= 1
        
        return res, resLen
```
