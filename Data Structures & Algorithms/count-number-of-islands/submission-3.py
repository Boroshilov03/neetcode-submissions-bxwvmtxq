import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:  # Correcting List import and syntax for Python 3.9+
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        return islands
