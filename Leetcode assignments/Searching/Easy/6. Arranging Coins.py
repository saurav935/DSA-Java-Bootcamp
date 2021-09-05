
# Optimized solution - O(logn)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1

        l = 0
        r = n- 1
        while l <= r:
            mid = l + (r - l) // 2
            formula = ((mid + 1) * (mid + 2)) // 2
            if formula > n:
                r = mid - 1
            elif formula < n:
                l = mid + 1
            else:
                return mid + 1
        return r + 1


# Brute force - O(n)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = 0
        if n == 1:
            return 1
        for i in range(1, n + 1):
            total += i
            if total > n:
                return i - 1

