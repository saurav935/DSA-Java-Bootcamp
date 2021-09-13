
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 1
        r = len(nums)

        while l <= r:
            mid = l + ( r -l) // 2
            count = self.count(nums ,mid)
            if count > mid:
                l = mi d +1

            elif count < mid:
                r = mi d -1

            else:
                return mid
        return -1


    def count(self ,nums ,n):
        count = 0
        for i in nums:
            if i >= n:
                count += 1
        return count