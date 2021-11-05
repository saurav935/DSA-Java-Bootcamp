# 1st solution:

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        arr = []
        
        for i in range(0,len(s)):   # len(s) == len(t)
            arr.append(abs(ord(t[i]) - ord(s[i])))
        
        i = 0
        j = 0
        summ = 0
        
        while j < len(arr):
            summ += arr[j]
            
            if summ > maxCost:
                while summ > maxCost:
                    summ -= arr[i]
                    i += 1
                    
            elif summ <= maxCost:
                ans = max(ans,j-i+1)
                
            j += 1
            
        return ans


    
# 2nd solution:

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        
        for j in range(0,len(s)):
            maxCost -= abs(ord(t[j]) - ord(s[j]))
        
            if maxCost < 0:
                maxCost += abs(ord(t[i]) - ord(s[i]))
                i += 1
                
        return j - i + 1
        
        
