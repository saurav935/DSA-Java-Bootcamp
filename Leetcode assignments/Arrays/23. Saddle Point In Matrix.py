

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_set = set()
        max_set = set()

        for r in matrix:
            min_set.add(min(r))

        for c in zip(*matrix):
            max_set.add(max(c))

        if min_set & max_set:
            return list(min_set & max_set)
        else:
            return []

