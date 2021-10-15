# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = -float('inf')
        b = -float('inf')
        
        for i in nums:
            if i >= a:
                b = a
                a = i
            elif i > b:
                b = i
                
        return (a-1) * (b-1)
    

    

# Time complexity - O(nlogn)
# Space complexity - O(n)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums,reverse=True)
        product = (nums[0]-1) * (nums[1]-1)
        
        return product
