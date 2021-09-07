
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.pivot_finder(nums)

    def pivot_finder(self, arr):
        l = 0
        r = len(arr) - 1

        while l != r:  # or l <= r
            mid = l + (r - l) // 2

            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l