class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        rounds = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
        
        def process_grid_cell(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or grid[r][c] == 0:
                return
            grid[r][c] = 2
            queue.append((r, c))
            visited.add((r, c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                process_grid_cell(r + 1, c)
                process_grid_cell(r - 1, c)
                process_grid_cell(r, c + 1)
                process_grid_cell(r, c - 1)
            rounds += 1
        rounds -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return max(rounds, 0)