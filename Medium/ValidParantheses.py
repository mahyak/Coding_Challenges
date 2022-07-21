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
          
      
