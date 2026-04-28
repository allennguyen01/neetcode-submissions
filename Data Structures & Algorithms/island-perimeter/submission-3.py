class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(i, j):
            q = deque([(i, j)])
            visit = set([(i, j)])
            res = 0

            while q:
                # print(q, i, j)
                i, j = q.popleft()
                
                for x, y in directions:
                    nx = i + x
                    ny = j + y
                    if nx < 0 or ny < 0 or nx > (ROWS-1) or ny > (COLS-1) or grid[nx][ny] == 0:
                        res += 1
                        continue
                    if grid[nx][ny] == 1 and (nx, ny) not in visit:
                        visit.add((nx, ny))
                        q.append((nx, ny))

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    return bfs(i, j)

        return 0