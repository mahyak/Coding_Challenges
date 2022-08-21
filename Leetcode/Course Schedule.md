Course Schedule (Leetcode #207)
===============================
### Medium
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

### Example 1:

Input: `numCourses = 2, prerequisites = [[1,0]]`
Output: `true`
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
### Example 2:

Input: `numCourses = 2, prerequisites = [[1,0],[0,1]]`
Output: `false`
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


### Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
`1 <= numCourses <= 10^5`

Solution
========
###1 - Build a graph based on the adjacency list representation
###2 - if there is cysle in graph :return False, 
###      else: return True

```python
###1 - Build a graph based on the adjacency list representation
###2 - if there is cysle in graph :return False, 
###      else: return True
# TimeComplexity: O(n+p)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # convert problem to graph by using dic, key = crs, values = [pre1, pre2, ...]
        preMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitedSet = set()
        
        #detect loop in graph
        def dfs(crs):
            if crs in visitedSet:
                return False
            
            if preMap[crs] == []:
                return True
            
            visitedSet.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visitedSet.remove(crs)
            preMap[crs] = []
            
            return True
        
        # check if crs created seperate graphs 1->2, 3->4
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
```
tags: cyclic, cycle, dfs
