class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])


        #1. Capture unsurrounded regions (0 -> T)
        directions = [(0,1), (0,-1), (1, 0), (-1,0)]
        def capture(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return

            board[r][c] = 'T'
            
            for nr, nc in directions:
                capture(r + nr, c + nc)

        #2. Capture surrounded regions ( O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0,cols-1]):
                    capture(r,c)
        #3. Uncapture
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
