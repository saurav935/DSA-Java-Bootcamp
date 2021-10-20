class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        
        for i in range(0,len(word)):
            if word_list[i] == ch:
                break
        
        if word_list[i] == ch:
            return "".join(word_list[:i+1][::-1]) + "".join(word_list[i+1:])
        else:
            return word
            
