class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not(0 <= r < ROWS) or not(0 <= c < COLS) or board[r][c] != word[i] or board[r][c] == "#":
                return False
            board[r][c] = "#"
            res =  dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r + 1, c, i + 1) or dfs(r , c + 1, i + 1)
            board[r][c] = word[i]
            return res


        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False

