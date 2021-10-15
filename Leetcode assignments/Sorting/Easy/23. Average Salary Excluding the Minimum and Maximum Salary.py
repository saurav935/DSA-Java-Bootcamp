# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def average(self, salary: List[int]) -> float:
        min_element = min(salary)
        max_element = max(salary)
        summ = 0
        
        for i in salary:
            if i != min_element and i != max_element:
                summ += i
                
        return summ / (len(salary)-2)
        
