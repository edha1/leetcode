class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        n = len(prices)
        
        # 1. Compute max profit if we only do one transaction up to day i (from left)
        leftProfits = [0] * n
        minPrice = prices[0]
        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            leftProfits[i] = max(leftProfits[i-1], prices[i] - minPrice)

        # 2. Compute max profit if we only do one transaction starting from day i (from right)
        rightProfits = [0] * n
        maxPrice = prices[-1]
        for i in range(n-2, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            rightProfits[i] = max(rightProfits[i+1], maxPrice - prices[i])

        # 3. Combine results to find max sum of profits from two transactions
        maxTotalProfit = 0
        for i in range(n):
            maxTotalProfit = max(maxTotalProfit, leftProfits[i] + rightProfits[i])

        return maxTotalProfit
