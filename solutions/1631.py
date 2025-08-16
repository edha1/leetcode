import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        distances = [[float("inf")] * cols for _ in range(rows)]
        distances[0][0] = 0
        
        min_heap = [(0, 0, 0)] 
        
        while min_heap:
            effort, x, y = heapq.heappop(min_heap)
            
            if x == rows - 1 and y == cols - 1:
                return effort
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    next_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    
                    if next_effort < distances[nx][ny]:
                        distances[nx][ny] = next_effort
                        heapq.heappush(min_heap, (next_effort, nx, ny))
