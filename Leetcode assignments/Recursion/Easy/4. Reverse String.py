class Solution:
    def reverseString(self, s: List[str]) -> None:
        return self.rev(s ,0 ,len(s ) -1)

    def rev(self ,s ,l ,r):
        if l > r:
            return s

        else:
            s[l] ,s[r] = s[r] ,s[l]
            return self.rev(s , l +1 , r -1)
