class Solution:
    def reverseWords(self, s: str) -> str:
        S = s.split()
        
        for i in range(0,len(S)):
            S[i] = S[i][::-1]

        return " ".join(S)
        
