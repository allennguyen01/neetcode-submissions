class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.m = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                val = self.m[i][j]
                total += val

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
