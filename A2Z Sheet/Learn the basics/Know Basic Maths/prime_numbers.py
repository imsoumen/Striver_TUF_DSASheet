import math
class Solution:
    def divisors(self, n):
        div = []
        
        sq = int(math.sqrt(n))

        for i in range(1, sq+1):
            if n%i == 0:
                div.append(i)

                if i != n // i:
                    div.append(n // i)
        
        return div
    
    def isPrime(self, n):
        #your code goes here
        if len(self.divisors(n)) > 2 or n == 1: return False
        return True

# TC: O(sqrt(n))
# SC: O(d) where d is number of divisors
