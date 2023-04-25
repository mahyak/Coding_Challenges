
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
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        if n != 0:
            stack = [("(", 1, 0)]
            while stack:
                s, open_cnt, close_cnt = stack.pop()
                
                if open_cnt == close_cnt == n:
                    result.append(s)
                if open_cnt < n:
                    stack.append((s+'(', open_cnt+1, close_cnt))
                if close_cnt < open_cnt:
                    stack.append((s+")", open_cnt, close_cnt+1))
        return result
   
# T: O(4^n/sqrt(n))
# S: O(n)              
```               
            
                
        
