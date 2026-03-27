class Solution:
    def recursion(self, arr, left, right):
        if left >= right:
            return
        
        arr[left], arr[right] = arr[right], arr[left]
        self.recursion(arr, left+1, right-1)

    def reverse(self, arr: list, n: int) -> None:
        self.recursion(arr, 0, n-1)

# TC: O(N)
# SC: O(N)