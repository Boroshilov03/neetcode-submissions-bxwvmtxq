class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        matrx = 
        [
          [1,2,4,8],
          [10,11,12,13],
          [14,20,30,40]
        ]
        target = 10
        '''
        if not matrix:
            return False

        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        top, bot = 0, rows

        while top <= bot:
            center = (top + bot) // 2
            if target > matrix[center][cols]:
                top = center + 1
            elif target < matrix[center][0]:
                bot = center - 1
            else:
                break

        middle = (top + bot) // 2

        l, r = 0, cols

        while l <= r:
            mid = (l+r) // 2
            if target > matrix[middle][mid]:
                l = mid + 1
            elif target < matrix[middle][mid]:
                r = mid - 1
            else:
                return True

        return False




