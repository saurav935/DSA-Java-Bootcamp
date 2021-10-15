class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(list(set(arr)))
        hashmap = {}
        
        for i in range(0,len(arr_sorted)):
            hashmap[arr_sorted[i]] = i+1
            
        nums = []
        
        for j in range(0,len(arr)):
            nums.append(hashmap[arr[j]])
        
        return nums


#######################################################


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap = {}
        nums = []
        
        for i in sorted(arr):
            if i not in hashmap:
                hashmap[i] = len(hashmap) + 1
                
        for j in arr:
            nums.append(hashmap[j])
        
        return nums
        
