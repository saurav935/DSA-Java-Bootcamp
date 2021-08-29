
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        summ = 0
        mid_row = row // 2
        mid_col = col // 2

        for r in range(0 ,row):
            summ += mat[r][r]

        i = 0
        for c in range(ro w -1 ,-1 ,-1):
            summ += mat[i][c]
            i += 1

        if row % 2 != 0:
            summ -= mat[mid_row][mid_col]

        return summ