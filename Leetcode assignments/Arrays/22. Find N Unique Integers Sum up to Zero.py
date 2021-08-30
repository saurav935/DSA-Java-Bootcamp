
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        mid = n // 2
        arr = [x for x in range(-mid, mi d +1)]

        if n % 2 == 0:
            arr.remove(0)
            return arr

        else:
            return arr

