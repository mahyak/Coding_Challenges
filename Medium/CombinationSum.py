class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        
        candidates.sort()
        result = []
        results = []
        
        self.dfs(candidates, result, results, target, 0)
        
        return results
    
    def dfs(self, candidates, result, results, target, start):
        if target == 0:
            results.append(result.copy())
            return results
        
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            result.append(candidates[i])
            self.dfs(candidates, result, results, target-candidates[i], i)
            result.pop(len(result)-1)
        
