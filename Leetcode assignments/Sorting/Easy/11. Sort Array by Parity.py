
# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums ) -1

        while i < j:
            while i < len(nums) and nums[i] % 2 == 0:
                i += 1

            while j > 0 and nums[j] % 2 != 0:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        return nums