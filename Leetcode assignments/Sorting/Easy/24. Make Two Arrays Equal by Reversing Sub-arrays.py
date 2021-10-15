# Time complexity - O(nlogn)
# Space complexity - O(1)

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        
        return target == arr



# Time complexity - O(n)
# Space complexity - O(n)

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_count = {}
        arr_count = {}
        
        for i in range(0,len(target)):
            if target[i] not in target_count:
                target_count[target[i]] = 1
            else:
                target_count[target[i]] += 1
                
            if arr[i] not in arr_count:
                arr_count[arr[i]] = 1
            else:
                arr_count[arr[i]] += 1

        return target_count == arr_count
        
