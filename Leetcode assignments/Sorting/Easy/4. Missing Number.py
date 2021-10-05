
# Amazon question
# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == n:
                i += 1
                continue
            elif nums[i] != i:
                self.swap(nums ,i ,nums[i])
            else:
                i += 1

        for j in range(0 ,n):
            if j != nums[j]:
                return j
        return n


    def swap(self ,arr ,i ,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

