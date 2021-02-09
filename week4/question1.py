class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        lo = 0
        hi = len(nums)-1
        while lo+1<hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                lo = mid
            else:
                hi = mid
        if nums[lo] >= target:
            return lo
        if nums[hi] <target:
            return hi+1
        else:
            return hi