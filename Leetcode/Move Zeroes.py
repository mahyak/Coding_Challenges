class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)
        
        while i < j:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                j -= 1
            else:
                i += 1
