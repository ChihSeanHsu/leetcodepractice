############### find max and loop to compare other###############
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max = 0
        for index, i in enumerate(nums):
            if Max < i :
                Max = i
                Maxin = index
                
        for index, i in enumerate(nums):
            if Max < i*2 and Maxin != index:
                return -1
            
        return Maxin
        
        
########### use python list function ###############       
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        max_1 = max(nums)
        max_i = nums.index(max_1)
        del nums[max_i]
        max_2 = max(nums)
        
        return max_i if max_1>=max_2*2 else -1
