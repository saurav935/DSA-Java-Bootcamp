# Time complexity - O(n)
# Space complexity - O(n)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashmap = {}
        
        for idx,num in enumerate(sorted(nums)):
            hashmap.setdefault(num, idx)
            
        return [hashmap[nums[j]] for j in range(0,len(nums))]



# Time complexity - O(n^2)
# Space complexity - O(n)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        
        for i in range(0,len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            arr.append(count)
            
        return arr
        
