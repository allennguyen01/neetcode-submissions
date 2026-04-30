class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def bfs(i, j):
            q = deque([(i,j)])
            grid[i][j] = '0'

            while q:
                i, j = q.popleft()

                for x, y in directions:
                    dx = i+x
                    dy = j+y
                    if dx < 0 or dx >= ROWS or dy < 0 or dy >= COLS or grid[dx][dy] == '0':
                        continue

                    grid[dx][dy] = '0'
                    q.append((dx,dy))

        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1

        return islands
                