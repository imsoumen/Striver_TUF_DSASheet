class Solution:
    def bubbleSort(self, nums):
        for i in range(len(nums)-1,-1,-1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        
        return nums

# TC: O(N^2)
# SC: O(1)