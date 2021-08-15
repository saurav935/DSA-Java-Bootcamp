# Optimised solution, time complexity-O(nlogn), space complexity-O(n)


def smallerNumbersThanCurrent(nums):
    count = {}

    for index, number in enumerate(sorted(nums)):
        count.setdefault(number, index)

    return [count[i] for i in nums]


# Brute force solution, time complexity-O(n^2), space complexity-O(n)

def smallerNumbersThanCurrent(nums):
    hashmap = {}
    arr = [0] * len(nums)

    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    for j in range(0, len(nums)):
        for key, value in hashmap.items():
            if key < nums[j]:
                arr[j] = arr[j] + value

    return arr
