
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        arr = []

        for i in nums:
            summ += i
            arr.append(summ)

        return arr


