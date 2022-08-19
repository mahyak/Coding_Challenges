Word Break (Leetcode #139)
===============================
### Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Solution
========
![img1](https://raw.githubusercontent.com/mahyak/Coding-Challenges/main/buttomup.png)
![Memoization approach](https://raw.githubusercontent.com/hamidb/interview-questions/master/leetcode/images/image0010.png)

```python
class Solution:
# O(n^2) (DP bottom up)
def wordBreak(self, s, wordDict):
    starts = [0]
    for i in range(len(s)):
        for j in starts:
            if s[j:i+1] in wordDict:
                starts.append(i+1)
                break
    return starts[-1] == len(s)
  ================================================= 
# O(N*L) (Samle as above using Trie)
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for w in wordDict:
            self.add(w)
        seen = {}
        return self._wordBreak(s, seen)
        
    def _wordBreak(self, s, seen):
        if s == "":
            return True
        if s in seen:
            return seen[s]
        p = self.root
        for i in range(len(s)):
            if s[i] not in p.children:
                seen[s] = False
                return False
            p = p.children[s[i]]
            if p.isWord and self._wordBreak(s[i+1:], seen):
                seen[s] = True
                return True
        seen[s] = False
        return False
            
        
    def add(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isWord = True
        
```

tags: Bottom Up, dictionary, space separated, word break
