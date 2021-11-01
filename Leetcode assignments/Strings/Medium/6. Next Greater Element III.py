class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = list(map(int, str(n)))
        i = len(arr) - 2
        
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1
            
        if i < 0:
            return -1
        
        j = len(arr) - 1
        
        while j >= 0 and arr[j] <= arr[i]:
            j -= 1
            
        arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1:] = arr[i+1:][::-1]
        
        res = ""
        for k in arr:
            res += str(k)
            
        res = int(res)
        
        if res > n and res < 2**31:
            return res
        else:
            return -1
        
