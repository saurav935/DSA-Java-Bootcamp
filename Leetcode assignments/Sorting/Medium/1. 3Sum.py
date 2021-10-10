
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3 or nums == []:
            return []

        nums.sort()
        arr = []

        for i in range(0 ,len(nums ) -1):
            if i > 0 and nums[i] == nums[ i -1]:
                continue
            a = -nums[i]
            j = i+ 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] < a:
                    j += 1
                elif nums[j] + nums[k] > a:
                    k -= 1
                else:
                    if [-a, nums[j], nums[k]] not in arr:
                        arr.append([-a, nums[j], nums[k]])
                    j += 1
                    k -= 1

        return arr