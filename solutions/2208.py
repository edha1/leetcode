import heapq

class Solution(object):
    def halveArray(self, nums):
        initial_sum = sum(nums)
        max_heap = [-x for x in nums] 
        heapq.heapify(max_heap)

        target = initial_sum / 2.0
        ops = 0

        while initial_sum > target:
            largest = -heapq.heappop(max_heap)   # get max
            halved = largest / 2.0
            initial_sum -= (largest - halved)    # subtract only the reduction
            heapq.heappush(max_heap, -halved)
            ops += 1

        return ops
