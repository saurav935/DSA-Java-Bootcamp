
# 1st solution, time complexity - O(nlogn)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1 = sorted(nums1)
            common = []
            for i in nums2:
                ele = self.binary_search(0, len(nums1) - 1, nums1, i)
                if ele != -1 and ele not in common:
                    common.append(i)


        else:
            nums2 = sorted(nums2)
            common = []
            for j in nums1:
                ele = self.binary_search(0, len(nums2) - 1, nums2, j)
                if ele != -1 and ele not in common:
                    common.append(j)
        return common

    def binary_search(self, l, r, arr, target):
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                return arr[mid]
        return -1


# 2nd soution


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        arr = []
        for i in nums1:
            if i in nums2:
                arr.append(i)
        return arr


# 3rd solution

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
