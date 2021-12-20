class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start+2*i for i in range(0,n)]
        ans = arr[0]
        for num in arr[1:]:
            ans = ans ^ num
            
        return ans
