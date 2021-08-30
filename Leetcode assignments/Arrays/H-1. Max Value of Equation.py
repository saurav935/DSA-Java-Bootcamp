
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = collections.deque()
        res = -float('inf')

        for j in range(0 ,len(points)):
            while q and points[j][0] - q[0][1] > k:
                q.popleft()

            if q:
                res = max(res, q[0][0] + points[j][1] + points[j][0])

            while q and q[-1][0] <= points[j][1] - points[j][0]:
                q.pop()

            q.append([points[j][1] - points[j][0], points[j][0]])

        return res



# Brute force approach, gives TLE
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        values = []

        for i in range(0 ,len(points ) -1):
            for j in range( i +1 ,len(points)):
                if abs(points[i][0] - points[j][0]) <= k:
                    value_of_eq = points[i][1] + points[j][1] + abs(points[i][0] - points[j][0])
                    values.append(value_of_eq)

        return max(values)
