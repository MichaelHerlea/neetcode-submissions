class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        dp = {}
        def dfs(r: int, c: int, max_val: int) -> int:
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or matrix[r][c] <= max_val:
                return 0

            if (r, c) not in dp:
                value = matrix[r][c]

                dp[(r, c)] = 1 + max(dfs(r + 1, c, value),
                    dfs(r - 1, c, value),
                    dfs(r, c + 1, value),
                    dfs(r, c - 1, value))
            
            return dp[(r, c)]
        
        output = 0
        for r in range(ROWS):
            for c in range(COLS):
                output = max(output, dfs(r, c, -1))
        
        return output