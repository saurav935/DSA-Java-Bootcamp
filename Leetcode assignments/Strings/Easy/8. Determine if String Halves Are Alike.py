class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        a = 0
        b = 0
        
        i = 0
        j = len(s)-1
        
        while i < j:
            a += s[i] in vowels
            b += s[j] in vowels
            i += 1
            j -= 1
            
        return a == b
        


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        first = s[:n//2]
        second = s[n//2:]
        
        first_count = 0
        second_count = 0
        
        for i in range(0,n//2):
            if first[i] in 'aeiou' or first[i] in 'AEIOU':
                first_count += 1
                
            if second[i] in 'aeiou' or second[i] in 'AEIOU':
                second_count += 1
            
        return first_count == second_count
