import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:  # Correcting List import and syntax for Python 3.9+
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
             
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc  # Using row and col correctly
                    if (new_row) in range(rows) and (new_col) in range(cols) and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
                    
        return islands
