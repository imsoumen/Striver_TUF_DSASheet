class Solution:
    def recursion(self, curr, n):
        if curr > n:
            return
        
        self.recursion(curr+1, n)
        print(curr)


    def printNumbers(self, n):
        # Your code goes here
        self.recursion(1, n)

# TC: O(N)
# SC: O(N)