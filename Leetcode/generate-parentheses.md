
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
from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = deque()
        for n in range(0, n):
            if n == 0:
                q.append('()')
            else:   
                length = len(q)
                
                while length>0:
                    length -= 1
                    value = q.popleft()
                    if  '()' + value != value + '()':
                        q.append(value + '()')
                    q.append('()' + value)
                    q.append('('+value+')')
        return q
```           
                
            
                
        
