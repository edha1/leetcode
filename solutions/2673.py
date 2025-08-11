class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """

        ans = 0
        for i in range(n // 2 - 1, -1, -1): # iterate from the leaves 
            left, right = i * 2 + 1, i * 2 + 2
            ans += abs(cost[left] - cost[right])
            cost[i] += max(cost[left], cost[right])
        return ans
        

        