class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        
        a = abs(dividend)
        b = abs(divisor)
        
        while a >= b:
            temp = b
            mul = 1
            
            while a >= temp:
                a -= temp
                ans += mul
                mul += mul
                temp += temp
                
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            return -ans
                
        return min(2147483647,max(-2147483648,ans))
            
