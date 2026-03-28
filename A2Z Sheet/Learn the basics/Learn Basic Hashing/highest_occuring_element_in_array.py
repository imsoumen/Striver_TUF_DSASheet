class Solution:
    def mostFrequentElement(self, nums):

        cnt_dict = {}

        for num in nums:
            if num not in cnt_dict:
                cnt_dict[num] = 1
            else:
                cnt_dict[num] += 1

        maxFreq = -1
        maxItem = 0
        for num, cnt in cnt_dict.items():
            if cnt > maxFreq:
                maxFreq = cnt
                maxItem = num
            elif cnt == maxFreq:
                maxItem = min(maxItem,num)
        
        return maxItem
    
# TC: O(N)
# SC: O(N)