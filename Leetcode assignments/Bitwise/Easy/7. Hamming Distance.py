class Solution:
    def hammingDistance(self, x: int, y: int) -> int:          
        return bin(x^y).count('1')

    
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = '{:032b}'.format(x)
        bin_y = '{:032b}'.format(y)
        print(bin_x)
        print(bin_y)
        count = 0
        
        for i in range(0,32):
            if bin_x[i] != bin_y[i]:
                count += 1
        return count
