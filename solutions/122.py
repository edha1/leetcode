class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        maxP = 0
        currMax = 0

        while r < len(prices):
            if prices[l] >= prices[r]:
                maxP += currMax
                currMax = 0
                l = r
            else:
                if prices[r] - prices[l] < currMax: 
                    maxP += currMax 
                    currMax = 0 
                    l = r 
                else: 
                    currMax = prices[r] - prices[l]
            r += 1

        maxP += currMax 
        return maxP
