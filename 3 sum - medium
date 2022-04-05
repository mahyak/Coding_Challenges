class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = set()
        
        for index in range(len(nums)):
            target = -sorted_nums[index]
            start = index + 1
            end = len(nums) - 1
            
            while start < end:
                two_sum = sorted_nums[start] + sorted_nums[end]
                if two_sum < target: 
                    start += 1
                elif two_sum > target:
                    end -= 1
                else:
                    result.add((-target, sorted_nums[start], sorted_nums[end]))
                    start += 1
                    end -= 1
        return result
