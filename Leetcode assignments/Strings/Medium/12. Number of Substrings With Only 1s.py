#Time complexity - O(n)
#Space complexity - O(n)
class Solution:
    def numSub(self, s: str) -> int:        
        a = s.split("0")
        ans = 0
        
        for i in a:
            if i != "":
                ans += (len(i)*(len(i)+1)) // 2
        return ans % (10**9+7)


#Time complexity - O(n)
#Space complexity - O(1)
class Solution:
    def numSub(self, s: str) -> int:        
        ans = 0
        i = 0
        j = 0
        
        while i < len(s):
            while i < len(s) and s[i] != "1":
                i += 1

            j = i
            
            while j < len(s)-1 and s[j+1] == "1":
                j += 1
            
            if i != len(s):
                n = j-i+1
                ans += (n*(n+1)) // 2
                i = j+1
        
        return ans % (10**9+7)
