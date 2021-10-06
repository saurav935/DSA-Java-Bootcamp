# Amazon and Microsoft interview question
# Using cyclic sort
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                self.swap(nums,i,nums[i]-1)
            else:
                i += 1
                
        arr = []
        
        for j in range(0,len(nums)):
            if nums[j] != j+1:
                arr.append(nums[j])
        
        return arr
        
        
    
    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
        
        
        

# Time complexity - O(n)
# Space complexity - O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = []
        
        for i in nums:
            if nums[abs(i)-1] < 0:
                arr.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
                
        return arr
        
        
        

# Time complexity - O(n)
# Space complexity - O(n)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        arr = []
        
        for key,value in count.items():
            if value == 2:
                arr.append(key)
                
        return arr
