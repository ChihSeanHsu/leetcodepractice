class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        
        """
        
        n = len(nums)
        count = [0]*(n+1)
        for i in nums:
            count[i] += 1
        for x in range(1, n+1):
            if count[x] == 0:
   
