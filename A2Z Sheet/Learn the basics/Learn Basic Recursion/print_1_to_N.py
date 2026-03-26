class Solution:
    def recursion(self, curr, n):
        if curr > n:
            return
        
        print(curr)
        self.recursion(curr+1, n)


    def printNumbers(self, n):
        # Your code goes here
        self.recursion(1, n)
        

# TC: O(N)
# SC: O(N)