
# Formula to rotate matrix by 90 degrees:

for r in range(0 ,n):
    for c in range(0 ,r):
        mat[r][c] ,mat[c][r] = mat[c][r] ,mat[r][c]

for x in range(0 ,len(mat)):
    mat[x] = mat[x][::-1]


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        if n == 1:
            if mat[0] == target[0]:
                return True
            elif mat[0] != target[0]:
                return False

        count = 0
        while count <= 4: # check notes for explaination for this 4
            for r in range(0 ,n):
                for c in range(0 ,r):
                    mat[r][c] ,mat[c][r] = mat[c][r] ,mat[r][c]

            for x in range(0 ,len(mat)):
                mat[x] = mat[x][::-1]

            if mat == target:
                return True

            count += 1
        return False
