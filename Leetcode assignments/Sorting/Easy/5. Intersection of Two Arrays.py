
# Using intersection function
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set1.intersection(set2))



# Using 2-pointers
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        arr = []
        
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] not in arr:
                    arr.append(nums1[i])
                i += 1
                j += 1
                
            elif nums1[i] > nums2[j]:
                j += 1
            
            elif nums1[i] < nums2[j]:
                i += 1
                
        return arr
