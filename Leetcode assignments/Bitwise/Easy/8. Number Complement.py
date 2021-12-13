class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        bit = 1
        
        while temp > 0:
            num = num ^ bit
            bit <<= 1
            temp >>= 1
        
        return num
