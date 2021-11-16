class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.check(num,0)
    
    
    def check(self,n,count):
        if n == 0:
            return count
        else:
            if n % 2 == 0:
                n //= 2
            else:
                n -= 1
            
            count += 1
            
            return self.check(n,count)
            
