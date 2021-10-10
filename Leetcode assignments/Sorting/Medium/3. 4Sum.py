

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        arr = []
        n = len(nums)

        for i in range(0 , n -3):
            if i > 0 and nums[i] == nums[ i -1]:
                continue
            for j in range( i +1 , n -2):
                if j > i+ 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1

                while k < l:
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l]

                    if sum_ < target:
                        k += 1

                    elif sum_ > target:
                        l -= 1

                    else:
                        if [nums[i], nums[j], nums[k], nums[l]] not in arr:
                            arr.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

        return arr