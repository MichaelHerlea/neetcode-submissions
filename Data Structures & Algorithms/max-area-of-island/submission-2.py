class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_size = 0

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0 or (r, c) in visited:
                return 0
            else: # grid[r][c] == 1
                visited.add((r, c))
                output = 1
                output += dfs(r + 1, c)
                output += dfs(r - 1, c)
                output += dfs(r, c + 1)
                output += dfs(r, c - 1)
                return output

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                max_size = max(max_size, dfs(r, c))

        return max_size