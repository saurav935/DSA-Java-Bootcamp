class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1 or n == 0:
            return bool(n)
        else:
            if n < 0 or n % 3 != 0:
                return False
            else:
                n //= 3
                return self.isPowerOfThree(n)
