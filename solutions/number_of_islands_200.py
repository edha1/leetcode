# Number of islands 

from collections import deque 

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [[0,1],[0,-1],[-1,0],[1,0]] # get all searchable directions 
        visited = [[False for _ in row] for row in grid]
        islands = 0
        def bfs(i, j): 
            q = deque() 

            q.append([i,j])

            while q: 

                curr = q.popleft() 
                x = curr[0]
                y = curr[1]

                if not visited[x][y]: 
                    visited[x][y] = True 

                    for dx, dy in directions: 
                        nx , ny = x + dx, y + dy 

                        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == "1": 
                            q.append([nx, ny]) # add the thingy 
            return 

            
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                
                if grid[i][j] == "1": 
                    if not visited[i][j]: 
                        bfs(i, j)
                        islands += 1
        return islands 
                    