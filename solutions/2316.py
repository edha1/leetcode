class Solution(object):
    def countPairs(self, n, edges):
        visited = [False] * n
        adj = [[] for _ in range(n)] # use an adjacency list to avoid TLE 
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        components = []

        for i in range(n):
            if not visited[i]:
                stack = [i]
                comp_size = 0
                while stack:
                    node = stack.pop()
                    if not visited[node]:
                        visited[node] = True
                        comp_size += 1
                        for nei in adj[node]:
                            if not visited[nei]:
                                stack.append(nei)
                components.append(comp_size)

        total_pairs = 0
        sum_so_far = 0
        for size in components:
            total_pairs += size * sum_so_far
            sum_so_far += size

        return total_pairs
