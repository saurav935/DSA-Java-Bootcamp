class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        deque_1 = deque(sentence1.split())
        deque_2 = deque(sentence2.split())
        
        while deque_1 and deque_2 and deque_1[0] == deque_2[0]:
            deque_1.popleft()
            deque_2.popleft()
            
        while deque_1 and deque_2 and deque_1[-1] == deque_2[-1]:
            deque_1.pop()
            deque_2.pop()
            
        return not deque_1 or not deque_2
        
