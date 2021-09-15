
#  Using binary search
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = l + ( r -l) // 2

            if l == r:
                break
            if self.capacity(weights ,mid) <= days:
                r = mid
            else:
                l = mid + 1

        return mid




    def capacity(self ,nums ,n):
        summ = 0
        count_of_days = 0

        for i in nums:
            if summ + i > n:
                count_of_days += 1
                summ = i
            else:
                summ += i

        return count_of_days + 1