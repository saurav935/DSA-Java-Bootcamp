class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            last = n & 1
            if last == 1:
                count += 1
            n >>= 1
        return count


# Alternative solution
    
    
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n = n & (n-1)
            c += 1
        return c
      
