class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        edge_hashmap = {i: [] for i in range(n)}
        for a, b in edges:
            edge_hashmap[a].append(b)
            edge_hashmap[b].append(a)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in edge_hashmap[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n