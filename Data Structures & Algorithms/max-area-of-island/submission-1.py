class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islandArea = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        maxArea = 0
        q = deque()
        def bfs(r,c):  
            nonlocal islandArea
            grid[r][c] = 0
            q.append((r,c))
            while q:
                row, col = q.popleft()
                islandArea += 1
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0<= nr < rows and 0<=nc<cols and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
            return islandArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    islandArea = 0  # Reset islandArea for each new island
                    islandArea = bfs(r,c)
                    maxArea = max(maxArea, islandArea)
        return maxArea
        