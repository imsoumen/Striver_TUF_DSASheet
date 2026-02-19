class Solution:
    def countDigit(self, n):
        
        if n == 0: 
            return 1
        else:
            digit = 0

            while n > 0:
                digit += 1
                n = n//10

        return digit