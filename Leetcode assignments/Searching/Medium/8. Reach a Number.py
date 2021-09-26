
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        l = 1
        r = target

        while l < r:
            mid = l + ( r -l) // 2
            if self.enough(mid ,target):
                r = mid
            else:
                l = mid +1

        steps = l


        diff = steps * (step s+1) // 2 - target
        if diff % 2:
            steps += steps % 2 + 1
        return steps


    def enough(self ,n ,target):
        if n * (n+1) // 2 >= target:
            return True
        return False


