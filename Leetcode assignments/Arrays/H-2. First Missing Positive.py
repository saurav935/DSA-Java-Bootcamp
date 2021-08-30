
#  Solution taking linear time and constant space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

#  Clean up
        for i in range(0 ,len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums ) +1

#  Placing our marker
        for num in nums:
            num = abs(num)
            if num <= len(nums) and nums[num-1] > 0:
                nums[num-1] = -nums[num-1]

#  Final step
        for k in range(0 ,len(nums)):
            if nums[k] > 0:
                return k+ 1

        return len(nums) + 1


#  Solution taking linear time and linear space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(1, max(nums) + 2):
            if i not in nums:
                return i

        return 1


