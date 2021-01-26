class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import numpy as np
        n = len(nums)
        target, rem = divmod(sum(nums), 2)
        if rem: return False
        if n==0: return True

        dp = np.zeros((n+1, target+1), dtype=np.int64)
        dp[0,0]=1
        for i in range(1, n+1):
            wk = nums[i-1]
            for j in range(1, target+1):
                if j < wk:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - wk]
        return dp[n, target]