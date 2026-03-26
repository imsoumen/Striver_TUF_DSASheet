class Solution:
    def factorial(self, n):
        #Your code goes here
        if n <= 1:
            return 1

        return n * self.factorial(n-1)


# TC: O(N)
# SC: O(N)