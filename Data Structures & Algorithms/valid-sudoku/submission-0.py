class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        for i in range(ROWS):
            for j in range(COLS):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                numberBox = ((i//3)*3  + j//3)
                if num in boxs[numberBox]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxs[numberBox].add(num)
        return True
"""
        #verif row by row
        for i in range(ROWS):
            setRow = set()
            for j in range(COLS):
                num = board[i][j]
                if num == ".":
                    continue
                if num in setRow:
                    return False
                setRow.add(num)
        #verif col by col
        for j in range(COLS):
            setcol = set()
            for i in range(ROWS):
                num = board[i][j]
                if num == ".":
                    continue
                if num in setcol:
                    return False
                setcol.add(num)

        def verifbox(startRow, startCol):
            seen = set()
            for r in range(startRow, startRow + 3):
                for c in range(startCol, startCol + 3):
                    num = board[r][c]
                    if num == ".":
                        continue
                    if num in seen:
                        return False
                    seen.add(num)
            return True
        for i in range(9):

        #verif box by box (3,4)  (3 % 3 + 1) + (4%3 + 1) % 9
        setBox = set()
        i, j = 0, 0
"""


        
