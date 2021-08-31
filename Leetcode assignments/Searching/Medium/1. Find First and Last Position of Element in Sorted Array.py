
# Time complexity - O(logn)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        ans[0] = self.binary_search(nums, target, True)
        if ans[0] != -1:
            ans[1] = self.binary_search(nums, target, False)

        return ans

    def binary_search(self, arr, target, findStartIndex):
        ans = -1
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] > target:
                r = mid - 1

            elif arr[mid] < target:
                l = mid + 1

            else:
                ans = mid
                if findStartIndex:
                    r = mid - 1
                else:
                    l = mid + 1

        return ans


# Solved by self, can do better!
# Time complexity - O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                while nums[l] != target:
                    l += 1

                while nums[r] != target:
                    r -= 1

                if nums[l] == target and nums[r] == target:
                    return [l, r]

            elif nums[mid] < target:
                l = mid + 1

            elif nums[mid] > target:
                r = mid - 1

        if nums[l] == target and nums[r] == target:
            return [l, r]
        else:
            return [-1, -1]


# Time complexity - O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        arr = []
        arr1 = []

        if target not in nums:
            return [-1, -1]

        for i in range(0, n):
            if nums[i] == target:
                arr.append(i)
            else:
                continue

        arr1.append(min(arr))
        arr1.append(max(arr))

        return arr1
