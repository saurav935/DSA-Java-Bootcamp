class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 0:
            return bool(n)
        else:
            if n % 2 != 0:
                return False
            else:
                n //= 2
                return self.isPowerOfTwo(n)
