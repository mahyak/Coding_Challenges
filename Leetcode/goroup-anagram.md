```
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
```
 

Example 1:
```

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```
Example 2:
```
Input: strs = [""]
Output: [[""]]
```
Example 3:
```
Input: strs = ["a"]
Output: [["a"]]
```

Solution
=========
``` python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_result = {}
        
        for word in strs:
            sorted_str = "".join(sorted(word))
            
            if sorted_str in final_result:
                final_result[sorted_str].append(word)
            else:
                final_result[sorted_str] = [word]
        
        return list(final_result.values())
```
