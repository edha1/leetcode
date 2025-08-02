from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxOranges = 0 
        maxCoord = [] 
        directions = [[0,1],[0,-1],[1,0],[-1,0]] 
        time = 0  
        q = deque()
        visited = [[False for _ in row] for row in grid] 

        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 2: 
                    if visited[i][j] == False: 
                        q.append([i,j]) # add the rotting oranges 

        while q: 
            level_size = len(q)  # Number of nodes in current level

            for _ in range(level_size): 
                curr = q.popleft() 
                x = curr[0]
                y = curr[1]
                for dx, dy in directions: 
                    nx, ny = dx + x, dy + y 

                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 0 
                        q.append([nx, ny]) # append to the queue 
            time += 1


        # check if there are any remaining good oranges 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 1: 
                    return -1 


        if time == 0: 
            return 0 
        else: 
            return (time - 1)


        