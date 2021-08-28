
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        height = 0

        for i in gain:
            height += i
            ans = max(ans ,height)

        return ans