class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = len(max(words,key = len))
        j = 1
        ans = ""
        arr = []
        
        for i in range(0,max_len):
            for word in words:
                if i < len(word):
                    ans += word[i:j]
                    if j == max_len+1:
                        break
                else:
                    ans += " "
            
            arr.append(ans.rstrip())
            ans = ""
            
            if j == max_len+1:
                break
            else:
                j += 1
                
        print(max_len)
        return arr
        
