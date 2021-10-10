
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = defaultdict(list)

        for i in set(nums):
            counts[nums.count(i)].append(i)

        for j in counts:
            if len(counts[j]) > 1:
                counts[j] = sorted(counts[j])[::-1]

        counts_sorted = sorted(counts)
        arr = []

        for j in counts_sorted:
            for l in counts[j]:
                arr += [l] * j

        return arr