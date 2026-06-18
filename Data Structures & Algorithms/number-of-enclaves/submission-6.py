class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            seen.add((r, c))
            count = 1
            enclave = True

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc

                    if not (0 <= newRow < ROWS and 0 <= newCol < COLS):
                        enclave = False
                        continue

                    if (newRow, newCol) not in seen and grid[newRow][newCol] == 1:
                        count += 1
                        q.append((newRow, newCol))
                        seen.add((newRow, newCol))

            return count if enclave else 0
        result = 0
        seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == 1:
                    result += bfs(r, c)
        return result
