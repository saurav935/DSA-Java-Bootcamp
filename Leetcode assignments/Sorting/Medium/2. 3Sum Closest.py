
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0 ] +nums[1 ] +nums[2]

        for i in range(0 ,len(nums ) -2):
            j = i+ 1
            k = len(nums) - 1

            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]

                if sum_ == target:
                    return sum_

                if abs(sum_ - target) < abs(res - target):
                    res = sum_

                if sum_ < target:
                    j += 1
                elif sum_ > target:
                    k -= 1

        return res