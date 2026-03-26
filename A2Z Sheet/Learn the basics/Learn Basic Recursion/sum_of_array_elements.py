class Solution:
    def arraySum(self, nums, idx = 0):
        #your code goes here
        if idx >= len(nums):
            return 0

        return int(nums[idx]) + self.arraySum(nums, idx+1)
    

# TC: O(N)
# SC: O(N)