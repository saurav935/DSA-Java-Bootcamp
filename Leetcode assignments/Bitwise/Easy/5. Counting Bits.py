class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(0,n+1):
            arr.append(self.countOnes(i))
        return arr
    
    def countOnes(self,n):
        count = 0
        while n > 0:
            last = n & 1
            if last == 1:
                count += 1
            n >>= 1
        return count

# Time complexity - O(n)
# Space complexity - O(n)
# Efficient solution

class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]
        for i in range(1,n+1):
            arr.append(arr[i>>1] + int(i&1))
        return arr
