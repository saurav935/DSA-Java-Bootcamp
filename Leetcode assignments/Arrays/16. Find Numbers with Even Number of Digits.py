
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
    
    
    
############################################   OR   ############################################
    
    
    
    
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_of_even_numbered_digits = 0
        
        for i in nums:
            if self.check_even_number_of_digits(i):
                count_of_even_numbered_digits += 1
        
        return count_of_even_numbered_digits
        
        
    
    def check_even_number_of_digits(self,n):
        count = 0
        while n > 0:
            count += 1
            n = n // 10
            
        if count != 0 and count % 2 == 0:
            return True
        else:
            return False



############################################   OR   ############################################
        
        
        
        
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_of_even_numbered_digits = 0
        
        for i in nums:
            if self.check_even_number_of_digits(i):
                count_of_even_numbered_digits += 1
        
        return count_of_even_numbered_digits
        
        
    
    def check_even_number_of_digits(self,n):
        count = math.log10(n) + 1
        if int(count) % 2 == 0:
            return True
        else:
            return False


