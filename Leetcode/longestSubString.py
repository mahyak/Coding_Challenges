# abcabcbb
# checking edge: if len(s) == 1 -> return 1
# two pointers -> left: l = 0, right: r = 1
# while r < len(s):
#   check if s[r] in s[l:r] -> r+=1, update the longestSub
#   else: iterate through s since s[r] in s[l:r] -> l+=1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        longestSub = 0
        
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                longestSub = max(longestSub, len(s[l:r]))
            else: 
                while s[r] in s[l:r]:
                    l += 1
                    
        return longestSub
