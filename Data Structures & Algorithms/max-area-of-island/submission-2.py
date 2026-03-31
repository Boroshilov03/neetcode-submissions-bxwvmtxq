class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        curr_area = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c):
            nonlocal curr_area
            grid[r][c] = 0
            curr_area += 1

            for dr, dc in directions:
                if dr+r in range(rows) and dc+c in range(cols) and grid[dr+r][dc+c] == 1:
                    dfs(dr+r, dc+c)
            return curr_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_area = 0
                    dfs(r,c)
                    max_area = max(max_area, curr_area)
        
        return max_area