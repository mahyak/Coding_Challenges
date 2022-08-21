
```
Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, find the minimum number of conference rooms required.
```
### Example 1:
```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
```

### Example 2:
```
Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
```

Solution
========
``` python
# Actually, we are looking for maximium intervals,
# Seperate statr points and end points into the seperate lists
# sort them
# Time Complexity: O(NlogN)
# Space Complexity: O(N)
class interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end
    
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      start = [i.start for i in intervals]
      end = [i.end for i in intervals]
      
      res, count = 0, 0
      s, e = 0, 0
      
      while s < len(intervals):
        if start[s] < end[e]:
          count += 1
          s += 1
        else:
          count -= 1
          e += 1
          
         res = max(res, count)
        
       return res
```
