
# Time complexity - O(n)
# Space complexity - O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(0 ,len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+ nums[i])
            
        return True


# Time complexity - O(n)
# Space complexity - O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        reach = 0

        while i < n and i <= reach:
            reach = max(i + nums[i], reach)
            i += 1

        return i == n
    
    
