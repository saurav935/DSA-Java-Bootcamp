
#  Using binary search
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = 0
        r = len(nums ) -1

        while l < r:
            mid = l + ( r -l) // 2

            if mid >= nums[mid]:
                r = mid

            elif mid < nums[mid]:
                l = mi d +1

        return r


