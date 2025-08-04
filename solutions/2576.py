class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums) // 2
        res = 0

        while left < len(nums) // 2 and right < len(nums):
            if nums[left] * 2 <= nums[right]:
                res += 2  # we mark both indices
                left += 1  # move to next unmatched small number
            right += 1  # always move right pointer forward
        
        return res 