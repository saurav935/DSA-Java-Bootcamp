class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 1
        r = len(nums)
        
        while l <= r:
            mid = l + (r-l) // 2
            count = self.count(mid,nums)
            
            if count == mid:
                return mid
            
            elif count > mid:
                l = mid+1
            
            elif count < mid:
                r = mid-1
                
        return -1
        
    
    
    def count(self,n,arr):
        count = 0
        for i in arr:
            if i >= n:
                count += 1
        return count
        
