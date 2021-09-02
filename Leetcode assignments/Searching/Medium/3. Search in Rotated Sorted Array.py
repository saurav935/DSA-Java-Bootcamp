
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        pivot = self.pivot_finder(nums)
        print(pivot)
        if pivot == -1:
            return self.binary_search(nums, 0, len(nums) - 1, target)

        if nums[pivot] == target:
            return pivot

        if target >= nums[0]:
            return self.binary_search(nums, 0, pivot - 1, target)

        if target < nums[0]:
            return self.binary_search(nums, pivot + 1, len(nums) - 1, target)

    def pivot_finder(self, arr):
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if mid < r and arr[mid] > arr[mid + 1]:
                return mid
            if mid > l and arr[mid] < arr[mid - 1]:
                return mid - 1
            if arr[mid] <= arr[l]:
                r = mid - 1
            else:
                l = mid + 1

        return -1

    def binary_search(self, arr, l, r, target):

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1


