class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        cnt_dict = {}
        result = []

        for num in nums:
            if num not in cnt_dict:
                cnt_dict[num] = 1
            else:
                cnt_dict[num] += 1
        
        for num, cnt in cnt_dict.items():
            result.append([num, cnt])
        
        return result

# TC: O(N)
# SC: O(N)