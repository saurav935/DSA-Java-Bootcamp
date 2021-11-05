class Solution:
    def minimumLength(self, s: str) -> int:
        temp = None
        i = 0
        j = len(s) - 1
        
        while i < j and s[i] == s[j]:
            temp = s[i]
            
            while i < j and s[i] == temp:
                i += 1
                
            while i <= j and s[j] == temp:
                j -= 1
                
        return j-i+1
        
