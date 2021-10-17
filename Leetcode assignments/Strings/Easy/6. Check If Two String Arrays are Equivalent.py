class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_1 = ""
        word_2 = ""
        
        for i in word1:
            word_1 += i
            
        for j in word2:
            word_2 += j
                
        return word_1 == word_2
        
