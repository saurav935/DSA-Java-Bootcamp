
# Using cyclic sort

# Time complexity - O(n)
# Space complexity - O(1)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i ] -1]:
                self.swap(nums ,i ,nums[i ] -1)
            else:
                i += 1

        arr = []

        for j in range(0 ,len(nums)):
            if nums[j] != j+ 1:
                arr.append(nums[j])
                arr.append(j + 1)

        return arr

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

