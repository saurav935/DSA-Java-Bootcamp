
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        r = sum(nums)
        
        while l <= r:
            mid = l + (r - l) // 2
            if l == r:
                return mid
            
            if self.count(mid, nums) <= m:
                r = mid
            elif self.count(mid, nums) > m:
                l = mid + 1
    

    def count(self, n, arr):
        count = 0
        summ = 0
        for i in arr:
            if summ + i > n:
                count += 1
                summ = 0
                summ += i
            else:
                summ += i
        return count + 1
    
