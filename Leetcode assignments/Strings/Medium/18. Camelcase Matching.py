class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        arr = []
        for i in queries:
            arr.append(self.helper(i,pattern))
        return arr
    
    
    def helper(self,word,pattern):
        i = 0
        j = 0
        while i < len(word) or j < len(pattern):
            if j == len(pattern):
                while i < len(word):
                    if word[i].isupper():
                        return False
                    i += 1
            
            elif i == len(word):
                return False
            
            elif word[i] == pattern[j]:
                j += 1
            
            elif word[i].isupper() and word[i] != pattern[j]:
                return False
            
            i += 1
            
        return True
        
