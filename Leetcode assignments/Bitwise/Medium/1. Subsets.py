class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0,2**len(nums)):
            subset = []
            for j in range(0,len(nums)):
                if (i>>j) & 1 == 1:
                    subset.append(nums[j])
                    
            ans.append(subset)
    
        return ans
