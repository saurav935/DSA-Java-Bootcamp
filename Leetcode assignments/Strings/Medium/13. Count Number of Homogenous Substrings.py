# Time complexity - O(n)
# Space coplexity - O(1)

class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        i = 0
        j = 0
        
        while i < len(s):
            temp = s[i]
            j = i
            while j < len(s)-1 and s[j+1] == temp:
                j += 1
                
            n = j-i+1
            ans += (n*(n+1)) // 2
            
            i = j+1
            
        return ans % (10**9+7)
