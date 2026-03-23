# Brute Force:

class Solution:
    def divisors(self, n): 
        ans = []
        for i in range(1,n+1):
            if n%i == 0:
                ans.append(i)
        
        return ans
    
# TC: O(N)
# SC: O(sqrt(N))

# Optimal
import math
class Solution:
    def divisors(self, n):
        ans = []
        
        sq = int(math.sqrt(n))

        for i in range(1, sq+1):
            if n%i == 0:
                ans.append(i)

                if i != n // i:
                    ans.append(n // i)
        
        ans.sort()
        
        return ans

# TC: O(sqrt(N)) + O(K*Log(K))
# SC: O(sqrt(N))