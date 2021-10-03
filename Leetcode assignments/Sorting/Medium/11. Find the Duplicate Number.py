
# Linear time and constant space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums[abs(i ) -1] < 0:
                return abs(i)
            else:
                nums[abs(i ) -1] *= -1

