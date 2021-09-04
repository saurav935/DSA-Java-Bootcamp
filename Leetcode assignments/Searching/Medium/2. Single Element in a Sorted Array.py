

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        #  Boundary checks
        if len(nums) == 1: return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]

        # Pair index property

        l = 0
        r = len(nums ) -1

        while l <= r :
            mid = l + ( r -l) // 2

            if l <= mid <= r and nums[mid] != nums[mi d -1] and nums[mid] != nums[mi d +1]:
                return nums[mid]

            if mid % 2 == 0:
                if mid >= l and nums[mid] == nums[mi d -1]:
                    r = mid-1
                elif mid >= l and nums[mid] != nums[mi d -1]:
                    l = mid+1

            elif mid % 2 != 0:
                if mid >= l and nums[mid] == nums[mi d -1]:
                    l = mid+1
                elif mid <= r and nums[mid] == nums[mi d +1]:
                    r = mid-1


