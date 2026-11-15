class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            count = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    if (0<=row+dr<ROWS and 0<=col+dc<COLS and grid[row+dr][col+dc] == 1):
                        q.append((row+dr, col+dc))
                        grid[row+dr][col+dc] = 0
                        count += 1
            return count
        
        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    result = max(bfs(r, c), result)
                    
        return result