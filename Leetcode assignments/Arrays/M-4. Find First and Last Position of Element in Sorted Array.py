

def searchRange(nums,target):
    if nums == []:
        return [-1 ,-1]

    l = 0
    r = len(nums) - 1

    while l < r:
        mid = ( l +r) // 2

        if nums[mid] == target:
            while nums[l] != target:
                l += 1

            while nums[r] != target:
                r -= 1

            if nums[l] == target and nums[r] == target:
                return [l ,r]

        elif nums[mid] < target:
            l = mid + 1

        elif nums[mid] > target:
            r = mid - 1

    if nums[l] == target and nums[r] == target:
        return [l ,r]
    else:
        return [-1 ,-1]




#  Time complexity - O(n)
def searchRange(nums,target):
    n = len(nums)
    arr = []
    arr1 = []

    if target not in nums:
        return [-1,-1]

    for i in range(0,n):
        if nums[i] == target:
            arr.append(i)
        else:
            continue

    arr1.append(min(arr))
    arr1.append(max(arr))

    return arr1
