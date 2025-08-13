import heapq

class Solution(object):
    def longestDiverseString(self, a, b, c):
        max_heap = [] 
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0: # ensure the letters start with some count 
                heapq.heappush(max_heap, (count, char))
        
        result = []
        
        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            
            # alr 2 consecutive 
            if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
                if not max_heap:
                    break  
                
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)
                count2 += 1  # counts are negative
                
                if count2 != 0:
                    # only append if count is available 
                    heapq.heappush(max_heap, (count2, char2))
                
                heapq.heappush(max_heap, (count1, char1))  
            else:

                result.append(char1)
                count1 += 1 
                
                if count1 != 0:
                    heapq.heappush(max_heap, (count1, char1))
        
        return "".join(result)
