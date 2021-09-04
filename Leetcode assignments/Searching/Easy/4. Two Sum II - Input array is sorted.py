# Using binary-search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(0, len(numbers)):
            l = i + 1
            r = len(numbers) - 1
            diff = target - numbers[i]

            while l <= r:
                mid = l + (r - l) // 2

                if numbers[mid] == diff:
                    return [i + 1, mid + 1]

                elif numbers[mid] > diff:
                    r = mid - 1

                elif numbers[mid] < diff:
                    l = mid + 1


# Using 2-pointer method
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            summ = numbers[l] + numbers[r]
            if summ > target:
                r -= 1
            elif summ < target:
                l += 1
            else:
                return [l + 1, r + 1]



