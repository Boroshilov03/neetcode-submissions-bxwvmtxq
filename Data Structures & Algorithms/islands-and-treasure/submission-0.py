from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        steps = 1      
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        INF = 2147483647
        
        # Initialize queue and visited set with all starting points (cells with value 0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # BFS to update distances from the nearest '0' cell
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                        q.append((nr, nc))
                        grid[nr][nc] = steps  # Update with current distance (steps + 1)
            steps += 1
