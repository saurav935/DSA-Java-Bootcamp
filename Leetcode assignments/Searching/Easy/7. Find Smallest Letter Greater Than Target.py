
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l = 0
        r = len(letters ) -1
        while l <= r:
            mid = l + ( r -l) // 2

            if letters[mid] > target:
                r = mi d -1

            else:
                l = mi d +1

        return letters[l % len(letters)]
