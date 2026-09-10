class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_hashmap = {i: [] for i in range(n)}
        visited = set()
        counter = 0
        for a, b in edges:
            edge_hashmap[a].append(b)
            edge_hashmap[b].append(a)

        def dfs(value):
            if value in visited:
                return
            visited.add(value)
            for children in edge_hashmap[value]:
                dfs(children)
        
        for i in range(n):
            if i not in visited:
                counter += 1
                dfs(i)
        
        return counter
        