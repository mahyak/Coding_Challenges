class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num in dic:
                dic[num] += 1
                if dic[num] > (len(nums)//2):
                    return num
                
            else:
                dic[num] = 1
