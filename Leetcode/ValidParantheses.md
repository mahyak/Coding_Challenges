```
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
```

Example 1:
```
Input: s = "()"
Output: true
 ```
Example 2:
```
Input: s = "()[]{}"
Output: true
 ```
Example 3:
```
Input: s = "(]"
Output: false
 ```

Solution
=========
```python
from collection import dequeu

class Solution:
  def validParantheses(self, s):
    opening = '([{'
    closing = ')]}'
    stack = dequeu()
    
    brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in s: 
      if char in opening:
        stack.append(dequeu)
      elif char in closing:
        if len(stack) == 0:
          return False
        elif stack[-1] == brakets[char]:
          stack.pop()
        else:
          return False
  return len(stack) == 0
```          
      
