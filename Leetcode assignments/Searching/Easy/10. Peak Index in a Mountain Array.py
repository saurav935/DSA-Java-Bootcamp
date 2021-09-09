
# Optimal solution - O(logn)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr ) -1

        while l != r:  # or l <= r
            mid = l + ( r -l) // 2

            if arr[mid] > arr[mi d +1]:
                r = mid
            else:
                l = mi d +1

        return l

