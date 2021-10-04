
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = sorted(heights)
        count = 0

        for i in range(0 ,len(heights)):
            if arr[i] != heights[i]:
                count += 1

        return count