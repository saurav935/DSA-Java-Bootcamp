# Amazon interview question

# Using cyclic sort

# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums):
                i += 1
                continue

            if nums[i] != nums[nums[i ] -1]:
                self.swap(nums ,i ,nums[i ] -1)

            else:
                i += 1

        for j in range(0 ,len(nums)):
            if nums[j] != j+ 1:
                return j + 1

        return len(nums) + 1

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
