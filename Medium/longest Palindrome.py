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
