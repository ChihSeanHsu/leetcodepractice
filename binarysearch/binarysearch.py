class Solution:
    
    def loop(self, nums, target, mid):
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            mid += 1
            if mid > len(nums)-1:
                return -1
            elif nums[mid] > target:
                return -1
            else:
                return self.loop(nums, target, mid)
        elif nums[mid] > target:
            mid -= 1
            if mid < 0:
                return -1
            elif nums[mid] < target:
                return -1
            else:
                return self.loop(nums, target, mid)
            
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = int(len(nums)/2)
        
        
        return self.loop(nums, target, mid)
