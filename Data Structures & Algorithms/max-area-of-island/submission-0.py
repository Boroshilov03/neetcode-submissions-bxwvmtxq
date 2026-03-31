class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islandArea = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        maxArea = 0
        def dfs(r,c):
            nonlocal islandArea
            islandArea +=1
            grid[r][c] = 0
            for row, col in directions:
                nr = r + row
                nc = c + col
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    dfs(nr, nc)
            return islandArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    islandArea = 0  # Reset islandArea for each new island
                    islandArea = dfs(r,c)
                    maxArea = max(maxArea, islandArea)
        return maxArea
        