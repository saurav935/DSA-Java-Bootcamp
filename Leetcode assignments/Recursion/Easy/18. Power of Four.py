class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0 or n == 1:
            return bool(n)
        else:
            if n < 0 or n % 4 != 0:
                return False
            else:
                n //= 4
                return self.isPowerOfFour(n)
                
