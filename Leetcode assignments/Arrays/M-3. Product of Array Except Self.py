'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''


##   Most optimal solution, takes O(n) time and O(1) space, written by self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = 1
        right = [1]

        for j in nums[:0:-1]:
            right.append(right[-1] * j)

        right = right[::-1]

        for i in range(0, len(nums)):
            right[i] = right[i] * left
            left = left * nums[i]

        return right

#   Brute force, gives TLE
    def brute_force(self,nums):
        product = 1
        res = []

        for i in range(0, len(nums)):
            for j in range(0, i):
                product = product * nums[j]
            for k in range(i + 1, len(nums)):
                product = product * nums[k]
            res.append(product)
            product = 1
        return res



#    Solution taking O(n) time and space
    def suboptimal(self,nums):
        left = [1]
        right = [1]

        for i in nums[:-1]:
            left.append(left[-1] * i)

        for j in nums[:0:-1]:
            right.append(right[-1] * j)

        right = right[::-1]

        for k in range(0, len(nums)):
            nums[k] = left[k] * right[k]

        return nums

