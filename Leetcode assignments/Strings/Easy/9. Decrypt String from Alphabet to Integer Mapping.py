class Solution:
    def freqAlphabets(self, s: str) -> str:
        s_rev = s[::-1]
        res = ""
        i = 0
        
        while i < len(s):
            if s_rev[i] == "#":
                temp = ""
                i += 1
                temp += s_rev[i]
                i += 1
                temp += s_rev[i]
                
                res += chr(97 + int(temp[::-1]) - 1)
            
            else:
                res += chr(97 + int(s_rev[i])-1)
                
            i += 1
            
        return res[::-1]
        
        
