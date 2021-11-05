class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        product = [0] * (len(num1) + len(num2))
        end = len(product) - 1
        
        
        for i in num1[::-1]:
            temp_pos = end
            
            for j in num2[::-1]:
                product[temp_pos] += int(i) * int(j)
                product[temp_pos-1] += product[temp_pos] // 10
                product[temp_pos] %= 10
                
                temp_pos -= 1
                
            end -= 1
            
        
        i = 0
        
        while i < len(product) and product[i] == 0:
            i += 1
            
        return "".join(map(str,product[i:]))
