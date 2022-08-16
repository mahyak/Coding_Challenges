
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

###Example 1:
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```
###Example 2:
```
Input: n = 1
Output: ["()"]
```

### Solution
==========
TimeComplexity: 

```python
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
```           
                
            
                
        
