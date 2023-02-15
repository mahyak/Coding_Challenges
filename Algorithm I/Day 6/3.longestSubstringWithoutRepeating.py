class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        longest_substring = 0
        l, r = 0, 1

        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                longest_substring = max(longest_substring, r - l)
            else: 
                while s[r] in s[l:r]:
                    l += 1
        
        return longest_substring

# T: O(n)
# S: O(1)
