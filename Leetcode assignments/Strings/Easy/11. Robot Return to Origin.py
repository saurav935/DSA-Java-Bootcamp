class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up = 0
        left = 0
        
        for i in moves:
            if i == 'L':
                left += 1
            elif i == 'U':
                up += 1
            elif i == 'D':
                up -= 1
                
            else:
                left -= 1
            
        return up == 0 and left == 0
        
        
