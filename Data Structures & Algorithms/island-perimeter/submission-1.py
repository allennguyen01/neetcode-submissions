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
                # right neighbour
                if j < COLS - 1 and grid[i][j+1] == 1:
                    res -= 2
                # bottom neighbour
                if i < ROWS - 1 and grid[i+1][j] == 1:
                    res -= 2
                # print(i, j, res)

        return res
