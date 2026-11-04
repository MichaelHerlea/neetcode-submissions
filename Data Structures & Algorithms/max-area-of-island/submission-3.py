class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_size = 0

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0:
                return 0
            else:
                grid[r][c] = 0
                output = 1
                output += dfs(r + 1, c)
                output += dfs(r - 1, c)
                output += dfs(r, c + 1)
                output += dfs(r, c - 1)
                return output

        for r in range(ROWS):
            for c in range(COLS):
                max_size = max(max_size, dfs(r, c))

        return max_size