```
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.
```

Solution
========
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.readSeq(self.countAndSay(n-1))
            
    def readSeq(self, s):
        output = ""
        prev = s[0]
        prev_count = 0
        
        for x in range(len(s)):
            if s[x] == prev:
                prev_count += 1
            else:
                output += str(prev_count)
                output += str(prev)
                prev = s[x]
                prev_count = 1
        output += str(prev_count)
        output += str(prev)
        return output
```
