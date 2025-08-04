class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        visited = len(graph)
        res = [] 
        final = [] 
        self.recurse(graph, res, 0, final)
        return final 

    def recurse(self, grid, arr, index, final):
        arr.append(index)

        # Base case: reached the target node
        if index == len(grid) - 1: 
            final.append(list(arr))  # append a copy
        else:
            for neighbor in grid[index]:
                self.recurse(grid, arr, neighbor, final)

        arr.pop()  # backtrack

        





        