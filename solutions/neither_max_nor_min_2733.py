class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort() 

        for i in range(1, len(nums) - 1): 
            return nums[i]
        
        return -1 
        