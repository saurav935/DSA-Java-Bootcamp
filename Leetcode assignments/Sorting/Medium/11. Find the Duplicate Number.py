# Amazon interview question
# Using cyclic sort
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                self.swap(nums,i,nums[i]-1)
            else:
                i += 1
                
        for j in range(0,len(nums)):
            if nums[j] != j+1:
                return nums[j]
            
    
    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        



        
# Linear time and constant space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums[abs(i ) -1] < 0:
                return abs(i)
            else:
                nums[abs(i ) -1] *= -1

