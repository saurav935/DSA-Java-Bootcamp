
class Solution:
    def minEatingSpeed(self, piles, h):

        l = 1
        r = max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            if self.count(piles, mid) <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l

    def count(self, arr, n):
        count = 0
        for i in arr:
            if i % n != 0:
                count += (i // n) + 1
            else:
                count += (i // n)
        return count
