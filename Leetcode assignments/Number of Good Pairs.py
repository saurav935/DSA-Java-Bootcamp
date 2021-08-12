
'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''


# Brute Force approach
def numIdenticalPairs(self, nums: List[int]) -> int:
    count = 0

    for i in range(0 ,len(nums)):
        for j in range( i +1 ,len(nums)):
            if nums[j] == nums[i]:
                count += 1
    return count


# Optimal solution
def numIdenticalPairs_2(self, nums: List[int]) -> int:
    hashmap = {}
    for i in nums:
        if i not in hashmap:
            hashmap[i] = nums.count(i)

    total = 0

    for key ,value in hashmap.items():
        total += self.calculate(value)
    return total


# n(n-1)//2 gives the total number of pairs
def calculate(self ,n):
    formula = ( n *( n -1)) // 2
    return formula
