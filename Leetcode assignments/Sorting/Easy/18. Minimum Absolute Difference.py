class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        diff = float('inf')
        arr.sort()
        nums = []
        
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1]) < diff:
                nums.clear()
                nums.append([arr[i-1],arr[i]])
                diff = abs(arr[i]-arr[i-1])
            
            elif abs(arr[i]-arr[i-1]) == diff:
                nums.append([arr[i-1],arr[i]])
        
        return nums
      
