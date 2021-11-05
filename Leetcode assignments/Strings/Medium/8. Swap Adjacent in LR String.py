class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        A = [(letter, idx) for idx,letter in enumerate(start) if letter == 'L' or letter == 'R']
        B = [(letter, idx) for idx,letter in enumerate(end) if letter == 'L' or letter == 'R']
        
        if len(A) != len(B):
            return False
        
        for (s,i),(e,j) in zip(A,B):
            if s != e:
                return False
            
            if s == 'R':
                if i > j:
                    return False
                
            if s == 'L':
                if i < j:
                    return False
                
        return True
