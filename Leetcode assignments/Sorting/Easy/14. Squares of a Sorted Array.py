# Using 2-pointer method
# Time complexity - O(n)
# Space complexity - O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        i = 0
        j = len(nums)-1
        
        for k in range(len(nums)-1,-1,-1):
            if abs(nums[i]) > abs(nums[j]):
                arr[k] = nums[i]**2
                i += 1
            else:
                arr[k] = nums[j]**2
                j -= 1
                
        return arr
    
    

# Using sorting 
# Time complexity - O(nlogn)
# Space complexity - O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [x**2 for x in nums]
        return sorted(arr)
      
