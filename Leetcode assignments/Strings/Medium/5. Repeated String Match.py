import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_len = math.ceil(len(b) / len(a))
        
        for i in range(0,2):
            if b in a * (min_len+i):
                return min_len+i

        return -1
        
