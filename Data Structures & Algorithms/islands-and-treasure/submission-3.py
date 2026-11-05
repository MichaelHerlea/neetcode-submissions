class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        def add_room(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or grid[r][c] == -1:
                return
            queue.append((r, c))
            visited.add((r, c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        distance = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                grid[r][c] = distance
                add_room(r + 1, c)
                add_room(r - 1, c)
                add_room(r, c + 1)
                add_room(r, c - 1)
            
            distance += 1