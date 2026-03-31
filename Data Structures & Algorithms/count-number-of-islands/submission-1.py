import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:  # Correcting List import and syntax for Python 3.9+
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or (r,c) in visited:
                return
            directions = [(0,1), (0,-1), (1, 0), (-1,0)]
            visited.add((r,c))

            for direction in directions:
                new_r = r + direction[0]
                new_c = c + direction[1]
                dfs(new_r,new_c)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
        return islands