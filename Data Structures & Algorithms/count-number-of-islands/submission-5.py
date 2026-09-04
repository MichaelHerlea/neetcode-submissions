class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        visited_islands = set()

        def dfs(i, j):
            if (i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == '0' or (i, j) in visited_islands): return
            visited_islands.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' or (i, j) in visited_islands:
                    continue
                dfs(i, j)
                number_of_islands += 1

        return number_of_islands