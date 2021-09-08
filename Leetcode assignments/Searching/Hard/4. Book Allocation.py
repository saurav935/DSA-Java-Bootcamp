
class Solution:

    # Function to find minimum number of pages.
    def findPages(self ,A, N, M):
        l = max(A)
        r = sum(A)

        while l <= r:
            mid = l + ( r -l) // 2
            if l == r:
                return mid
            if self.count(mid ,A) > m:
                l = mid +1
            else:
                r = mid


    def count(self ,n ,arr):
        count = 0
        summ = 0
        for i in arr:
            if sum m +i > n:
                count += 1
                summ = i
            else:
                summ += i
        return count +1

