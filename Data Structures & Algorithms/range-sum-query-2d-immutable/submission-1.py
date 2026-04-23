class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0 for _  in range(cols + 1)] for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                curr = matrix[i][j]
                leftBoxPrefix = self.prefix[i+1][j]
                upperBoxPrefix = self.prefix[i][j+1]
                subtractBoxPrefix = self.prefix[i][j]
                self.prefix[i+1][j+1] = curr + leftBoxPrefix + upperBoxPrefix - subtractBoxPrefix 

        # print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # total = bottomRight - upper - left + upperLeft
        bottomRight = self.prefix[row2 + 1][col2 + 1]
        upper = self.prefix[row1][col2 + 1]
        left = self.prefix[row2 + 1][col1]
        upperLeft = self.prefix[row1][col1]
        total = bottomRight - upper - left + upperLeft

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
