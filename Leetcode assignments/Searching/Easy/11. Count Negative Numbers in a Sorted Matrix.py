
#  Optimized solution, time complexity - O(n + m)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = len(grid ) -1
        j = 0
        count = 0
        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                count += len(grid[0] ) -j
                i -= 1

            elif grid[i][j] >= 0:
                j += 1

        return count





#  Brute force solution, O(n^2)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for i in range(0 ,len(grid)):
            for j in range(0 ,len(grid[0])):
                if grid[i][j] < 0:
                    count += 1

        return count
