class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
# Frst part
        i = 0
        j = len(a) - 1
        while i < j and a[i] == b[j]:
            i, j = i + 1, j - 1
        s1 = a[i:j + 1]
        s2 = b[i:j + 1]

        
# Second part        
        i = 0
        j = len(a) - 1
        while i < j and b[i] == a[j]:
            i, j = i + 1, j - 1
        s3 = a[i:j + 1]
        s4 = b[i:j + 1]
        

# Final part
        for s in (s1,s2,s3,s4):
            if s == s[::-1]:
                return True
            
        return False
        
        
        

# Gives TLE
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        for i in range(0,len(a)):
            a_p = a[:i]
            a_s = a[i:]
            b_p = b[:i]
            b_s = b[i:]
            
            if (a_p + b_s) == (a_p + b_s)[::-1] or (b_p + a_s) == (b_p + a_s)[::-1]:
                return True
            
        return False

      
