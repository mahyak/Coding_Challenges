```
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
```
 

Example 1:
```
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
```
Example 2:
```
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
```

Solution
========
```python
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indices_sum = len(list2) + len(list1) - 2
        common = {}
        res = []
        
        for index, element in enumerate(list1):
            if element not in common:
                common[element] = index
        
        for index, element in enumerate(list2):
            if element in common:
                if (index + common[element]) < indices_sum:
                    res.clear()
                    res.append(element)
                    indices_sum = (index + common[element])
                    
                elif (index + common[element]) == indices_sum:
                    res.append(element)
                    
        return res
```
