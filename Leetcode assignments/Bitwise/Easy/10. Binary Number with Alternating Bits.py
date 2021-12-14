class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n & 1
        while n > 0:
            n >>= 1
            temp = n & 1
            if temp == last:
                return False
            else:
                last = n & 1
        return True
