class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        arr = []
        
        for i in range(0,len(arr2)):
            arr += [arr2[i]] * count[arr2[i]]
            count.pop(arr2[i])
            
        map_sorted = sorted(count)
        
        for j in range(0,len(map_sorted)):
            arr += [map_sorted[j]] * count[map_sorted[j]]
        
        return arr
            
