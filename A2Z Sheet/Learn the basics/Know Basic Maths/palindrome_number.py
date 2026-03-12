class Solution:
    def reverseNumber(self, n):
        revNum = 0
        while n != 0:
            unitDigit = n%10
            revNum = revNum*10 + unitDigit
            n = n//10
        
        return revNum

    def isPalindrome(self, n):

        if n == self.reverseNumber(n):
            return True
        return False

'''
TC : O(logN)
SC : O(1)
'''