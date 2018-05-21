class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        suml = sum(nums)
        n = len(nums)
        cursum = 0
        for i in range(0, n):
            if suml - nums[i] == 2 * cursum:
                return i
            cursum += nums[i]
        return -1
