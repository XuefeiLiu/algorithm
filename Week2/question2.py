class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp: O(n^2)
        """
        import numpy as np
        if not nums:
            return 0
        dp = np.zeros(len(nums), dtype=np.int64)
        dp[0] = 1
        ans = 1
        for i in range(1,len(nums)):
            maxval = 0
            for j in range(i):
                if nums[i]>nums[j]:
                    maxval = max(maxval,dp[j])
            dp[i] = maxval + 1
            ans = max(ans,dp[i])
            
        return ans

    def lengthOfLIS(self, nums):
        """
        using binary search to construct the dp
        dp
        """
        from bisect import bisect_left 
        dp = []
        if not nums:
            return 0
        dp.append(nums[0])
        for i in range(1,len(nums)):
            index = bisect_left(dp,nums[i])
            print(nums[i],index)
            if index==len(dp):
                dp.append(nums[i])
            else:
                dp[index] =nums[i]

        return len(dp)
   