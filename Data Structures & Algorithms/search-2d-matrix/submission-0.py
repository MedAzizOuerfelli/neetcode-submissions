class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        leftR, rightR = 0, ROWS - 1
        while  leftR <= rightR:
            midR = (leftR + rightR) // 2
            if matrix[midR][0] <= target <= matrix[midR][COLS - 1]:
                leftC, rightC = 0, COLS - 1
                while leftC <= rightC:
                    midC = (leftC + rightC) // 2
                    if matrix[midR][midC] == target:
                        return True
                    elif matrix[midR][midC] < target:
                        leftC = midC + 1
                    else:
                        rightC = midC - 1
                return False
            elif target < matrix[midR][0]:
                rightR = midR - 1
            else:
                leftR = midR + 1
        return False


                