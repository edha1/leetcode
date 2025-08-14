class Solution(object):
    def maximizeGreatness(self, nums):
        nums.sort()
        n = len(nums)
        greatness = 0
        j = 0  

        for i in range(n):
            while j < n and nums[j] <= nums[i]:
                j += 1
            if j < n:
                greatness += 1
                j += 1 

        return greatness
