import math


class Solution:

    def count_digits(self, n):
        if n == 0:
            return 1

        cnt = int(math.log10(n)) + 1
        return cnt

    def isArmstrong(self, n):
        sum_digit, copy = 0, n

        cnt = self.count_digits(n)

        while n > 0:
            last_digit = n % 10
            sum_digit += pow(last_digit, cnt)
            n = n // 10

        if sum_digit == copy:
            return True

        return False
    
# TC: O(log n) 
# SC: O(1)
