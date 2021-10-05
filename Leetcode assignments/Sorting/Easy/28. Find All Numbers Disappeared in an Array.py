
# Time complexity - O(n)
# Space complexity - O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = []

        for i in range(0 ,len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        for j in range(0 ,len(nums)):
            if nums[j] > 0:
                arr.append( j +1)

        return arr




# Time complexity - O(n)
# Space complexity - O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = []
        hashtable = {}

        for i in nums:
            hashtable[i] = -1

        for j in range(1 ,len(nums ) +1):
            if hashtable.get(j) == None:
                arr.append(j)

        return arr

