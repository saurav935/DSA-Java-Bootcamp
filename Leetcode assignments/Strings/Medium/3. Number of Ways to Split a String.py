class Solution:
    def numWays(self, s: str) -> int:
        hashmap = {}
        m = len(s)
        
        for i in range(0,len(s)):
            if s[i] == '1':
                hashmap[i] = 1
                
        n = len(hashmap)
        
        if n % 3 != 0:
            return 0
        
        if n == 0:
            return (m-2)*(m-1) // 2 % 1000000007
        
        partition = n // 3
        
        diff1 = 0
        diff2 = 0
        
        count1 = 1
        count2 = 1
        
        for i in hashmap:
            if count1 == partition:
                diff1 = i
            elif count1 == partition+1:
                diff1 = i - diff1
            if count2 == n-partition:
                diff2 = i
            elif count2 == n-partition + 1:
                diff2 = i - diff2

            count2 += 1
            count1 += 1
            
        return (diff1 * diff2) % (1000000007)
        
        
