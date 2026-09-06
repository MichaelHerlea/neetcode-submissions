class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:     
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[False] * COLS for _ in range(ROWS)]
        atlantic = [[False] * COLS for _ in range(ROWS)]

        def dfs(i, j, visited, prev_height):
            if (i < 0 or j < 0 or i >= ROWS or j >= COLS
                    or visited[i][j] or heights[i][j] < prev_height):
                return
            visited[i][j] = True
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

        for i in range(ROWS):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, COLS - 1, atlantic, heights[i][COLS - 1])
        for j in range(COLS):
            dfs(0, j, pacific, heights[0][j])
            dfs(ROWS - 1, j, atlantic, heights[ROWS - 1][j])

        return [[i, j] for i in range(ROWS) for j in range(COLS)
                if pacific[i][j] and atlantic[i][j]]