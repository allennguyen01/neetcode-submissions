class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS solution
        # when rotten fruit is found, start BFS
        # if empty cell or already rotten: don't add to queue
        # if fresh fruit: mark as visited and add to queue
        # count how many "rounds" of BFS was performed, that is result
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(rottenFruits):
            q = deque(rottenFruits)
            minutes = 0

            while q:
                hasInfected = False

                for _ in range(len(q)):
                    i, j = q.popleft()

                    for x, y in directions:
                        dx = i + x
                        dy = j + y

                        if (dx < 0 or dy < 0 or dx >= ROWS or dy >= COLS
                            or grid[dx][dy] == 0 or grid[dx][dy] == 2):
                            continue

                        hasInfected = True
                        grid[dx][dy] = 2
                        q.append((dx,dy))
                
                minutes += 1 if hasInfected else 0
                
            return minutes

        res = 0
        allRotten = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    allRotten.append((i,j))

        res = bfs(allRotten)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return res