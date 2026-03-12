class Solution:
    def reverseNumber(self, n):
        revNum = 0
        while n != 0:
            unitDigit = n%10
            revNum = revNum*10 + unitDigit
            n = n//10
        
        return revNum
    
'''
    TC : O(logN)
    SC : O(1)
'''