# Not the best solution

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        
        for i in range(left,right+1):
            count_of_set_bits = self.count_set_bits(i)
            
            if self.check_prime(count_of_set_bits):
                count += 1
                
        return count
    
    
    def count_set_bits(self,n):
        count = 0
        while n > 0:
            last = n & 1
            if last == 1:
                count += 1
            n >>= 1
        return count
        
    
    def check_prime(self,n):
        if n > 1:
            for i in range(2,(n//2)+1):
                if n % i == 0:
                    return False
            return True
        else:
            return False
            
