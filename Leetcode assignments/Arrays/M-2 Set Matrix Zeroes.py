

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []

        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[0])):
                if matrix[r][c] == 0:
                    row.append(r)
                    col.append(c)

        for a in row:
            for b in range(0, len(matrix[0])):
                matrix[a][b] = 0

        for i in col:
            for j in range(0, len(matrix)):
                matrix[j][i] = 0
