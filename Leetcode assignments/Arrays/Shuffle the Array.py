
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = len(nums) // 2
        arr1 = nums[:mid]
        arr2 = nums[mid:]

        result = []

        for i in range(0, len(
                arr1)):  # doesn't matter arr1 or arr2, as they are going to have the same length because our nums is of 2n (even) length.
            result.append(arr1[i])
            result.append(arr2[i])

        return result

