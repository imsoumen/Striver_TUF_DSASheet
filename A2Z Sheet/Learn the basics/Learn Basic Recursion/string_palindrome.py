class Solution:
    def recursion(self, arr, left, right):
        
        if left >= right:
            return True
        
        if arr[left] != arr[right]:
            return False
        
        return self.recursion(arr, left+1, right-1)

    def palindromeCheck(self, s):
        return self.recursion(s, 0, len(s)-1)
    
# TC: O(N)
# SC: O(N)
