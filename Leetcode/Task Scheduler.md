Task Scheduler (Leetcode #621)
===============================
### Medium

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order.
Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two same tasks (the same letter in the array),
that is that there must be at least `n` units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

### Example 1:
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```

### Example 2:
```
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
```

### Example 3:
```
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
``` 

### Constraints:
```
1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
```

Solution
========
```python
# T:O(26*log(26) * N)
# S: (26)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
        

# T: O(N)
# S: O(26)
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         # frequencies of the tasks
#         frequencies = [0] * 26
#         for t in tasks:
#             frequencies[ord(t) - ord('A')] += 1

#         # max frequency
#         f_max = max(frequencies)
#         # count the most frequent tasks
#         n_max = frequencies.count(f_max)

#         return max(len(tasks), (f_max - 1) * (n + 1) + n_max)
```
