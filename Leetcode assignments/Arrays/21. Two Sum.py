
#  Using enumerate function
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, value in enumerate(nums):
            if (target - value) in hashmap:
                return [idx, hashmap[target - value]]

            else:
                hashmap[value] = idx




#  Using for loop:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        hashmap = {}
        arr = []

        for i in range(0 ,n):
            if targe t -nums[i] in hashmap:
                arr.append(hashmap[targe t -nums[i]])
                arr.append(i)
                return arr

            else:
                hashmap[nums[i]] = i
