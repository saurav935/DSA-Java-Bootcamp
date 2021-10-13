# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_idx = 0
        odd_idx = len(nums)-1
        n = len(nums)
        
        while even_idx < n and odd_idx > 0:
            if nums[even_idx] % 2 == 0:
                even_idx += 2
            
            elif nums[odd_idx] % 2 != 0:
                odd_idx -= 2
                
            else:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
                even_idx += 2
                odd_idx -= 2
                
        return nums
        
