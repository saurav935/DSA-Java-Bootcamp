
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ""
        for i in num:
            s += str(i)

        answer = int(s) + k

        return  list("".join(str(answer)))


