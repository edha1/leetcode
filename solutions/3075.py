class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        

        max_heap = [] 
        total = 0 
        for i in range(len(happiness)): 
            heapq.heappush(max_heap, -happiness[i])

        total += heapq.heappop(max_heap) * -1
        curr = 0 
        for i in range(1, k): 
            if max_heap: 
                curr = heapq.heappop(max_heap) * -1 
                curr -= (i)
                if curr <= 0: 
                    return total 
                total += curr 
            else: 
                return total 

        return total 