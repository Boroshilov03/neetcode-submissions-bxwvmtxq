from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        BFS 
        Queue from deque

        iterate through all cells and add rotten oranges cordinates to the queue
        + fresh oranges

        cordinates = list of 4 directions, up down left right

        we popleft from the q
        and check all sides and add the cordinates of fresh ones to the list

        '''

        q = deque()
        freshFruits  = 0
        totalTime = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))

                if grid[r][c] == 1:
                    freshFruits += 1

        directions = [[0,1], [0, -1], [1,0], [-1,0]]
        
        while q and freshFruits > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                            freshFruits -= 1
            

            totalTime += 1 

        if freshFruits > 0:
             return -1

        return totalTime




        