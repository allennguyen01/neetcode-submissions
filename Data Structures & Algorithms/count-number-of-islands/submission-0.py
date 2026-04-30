class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i-1, j)

            return

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res