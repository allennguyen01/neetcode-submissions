class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                cell = grid[i][j]
                
                if cell != 1:
                    continue

                res += 4
                # left neighbour
                if j > 0 and grid[i][j-1] == 1:
                    res -= 1
                # right neighbour
                if j < COLS - 1 and grid[i][j+1] == 1:
                    res -= 1
                # top neighbour
                if i > 0 and grid[i-1][j] == 1:
                    res -= 1
                # bottom neighbour
                if i < ROWS - 1 and grid[i+1][j] == 1:
                    res -= 1
                # print(i, j, res)

        return res
