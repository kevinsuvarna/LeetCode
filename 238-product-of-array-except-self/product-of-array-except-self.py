class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        pref = [1] * n
        suff = [1] * n

        pref[0] = 1
        suff[n-1] = 1

        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        for i in range(n):
            res[i] = suff[i] * pref[i]

        return res