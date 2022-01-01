'''
# Brute force solution (gives memory limit exceeded error)
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        and_arr = []
        
        for i in range(0,len(arr1)):
            for j in range(0,len(arr2)):
                and_arr.append(arr1[i]&arr2[j])
                
        xor_arr = and_arr[0]
        
        for x in and_arr[1:]:
            xor_arr = xor_arr^x
            
        return xor_arr

''' 
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        arr_1_xor_sum = arr1[0]
        arr_2_xor_sum = arr2[0]
        
        for i in arr1[1:]:
            arr_1_xor_sum = arr_1_xor_sum ^ i
            
        for j in arr2[1:]:
            arr_2_xor_sum = arr_2_xor_sum ^ j
                        
        arr = []
        
        for i in range(0,len(arr1)):
            arr.append(arr_2_xor_sum & arr1[i])
            
        ans = arr[0]
        
        for k in arr[1:]:
            ans ^= k
            
        return ans
    
