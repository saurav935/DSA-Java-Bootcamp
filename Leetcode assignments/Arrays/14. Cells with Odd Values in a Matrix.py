
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        dup_indices = []
        for i in indices:
            dup_indices += i

        matrix = [[0 for p in range(0 ,n)]
                  for q in range(0 ,m)]


        for i in range(0 ,len(dup_indices)):
            if i % 2 == 0:
                matrix[dup_indices[i]] = self.change_row(matrix[dup_indices[i]])
            else:
                matrix = self.change_col(matrix ,dup_indices[i])

        count = 0

        for r in range(0 ,len(matrix)):
            for c in range(0 ,len(matrix[0])):
                if matrix[r][c] % 2 != 0:
                    count += 1

        return count


    def change_row(self ,arr):
        for i in range(0 ,len(arr)):
            arr[i] += 1
        return arr


    def change_col(self ,matrix ,col_num):
        for r in range(0 ,len(matrix)):
            matrix[r][col_num] += 1
        return matrix

