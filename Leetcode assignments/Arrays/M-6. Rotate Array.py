
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums ,0 ,len(nums ) -1)
        self.reverse(nums ,0 , k -1)
        self.reverse(nums ,k ,len(nums ) -1)

    def reverse(self ,arr ,start ,end):
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1


##############################   OR   ################################


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
