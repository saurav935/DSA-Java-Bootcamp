
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums == [0 ] *len(nums):
            return "0"

        for i in range(0 ,len(nums)):
            for j in range( i +1 ,len(nums)):
                num1 = int(str(nums[i]) + str(nums[j]))
                num2 = int(str(nums[j]) + str(nums[i]))

                if num2 > num1:
                    self.swap(nums ,i ,j)

        ans = ""

        for i in nums:
            ans += str(i)

        return ans


    def swap(self ,arr ,i ,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp