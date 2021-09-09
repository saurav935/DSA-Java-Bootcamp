
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #   Storing the count required for each element
        hashmap = {}
    if len(nums1) < len(nums2):
        for i in nums1:
            hashmap[i] = min(nums1.count(i) ,nums2.count(i))
    else:
        for j in nums2:
            hashmap[j] = min(nums1.count(j) ,nums2.count(j))


        #   Code to extract the common elements along with the condition
    if len(nums1) > len(nums2):
        nums1 = sorted(nums1)
        common = []
        for i in nums2:
            ele = self.binary_search(0 ,len(nums1 ) -1 ,nums1 ,i)
            if ele != -1 and common.count(ele) < hashmap[ele]:
                common.append(i)

    else:
        nums2 = sorted(nums2)
        common = []
        for j in nums1:
            ele = self.binary_search(0 ,len(nums2 ) -1 ,nums2 ,j)
            if ele != -1 and common.count(ele) < hashmap[ele]:
                common.append(j)
    return common



    #   Standard binary search algorithm
    def binary_search(self ,l ,r ,arr ,target):
        while l <= r:
            mid = l + ( r -l) // 2

            if arr[mid] > target:
                r = mi d -1
            elif arr[mid] < target:
                l = mi d +1
            else:
                return arr[mid]
        return -1