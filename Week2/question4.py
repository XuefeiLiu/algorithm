class Solution(object):
    def superEggDrop2(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        O(KN^2)
        """
        import numpy as np
        dp = np.zeros((K+1,N+1),dtype=np.int64)
        dp[:,1] = 1
        for i in range(1,N+1):
            dp[1,i] = i
        for i in range(2,K+1):
            for j in range(2,N+1):
                dp_min = np.inf
                for k in range(1,j+1):              
                    dp_k = max(dp[i-1,k-1],dp[i,j-k]) +1
                    dp_min = min(dp_k,dp_min)
                dp[i,j] = dp_min
        return dp[K,N]            
                    
        
        
    def superEggDrop(self, K, N):
        """
        O(K*NLOGN)
        """
        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) / 2
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)