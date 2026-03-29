class Solution:
    def selectionSort(self, nums):

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        
        return nums

# TC: O(N^2)
# SC: O(1)