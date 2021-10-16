class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s[::-1].split()
        words.sort()
        ans = []
        
        for i in words:
            ans.append(i[1:][::-1])
            
        return " ".join(ans)
    
    
# Using hashmap    
class Solution:
    def sortSentence(self, s: str) -> str:
        
        hashmap = {}
        s = s.split()
        result = ""

        for i in s:
            if i[-1].isdigit():
                hashmap[int(i[-1])] = i[:-1]

        a = sorted(hashmap)

        for q in range(1,len(a)+1):
            
            result += hashmap[q]
            
            if q != len(a):
                result += " "

        return result
