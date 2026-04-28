class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0

        while l <= r:
            m = (r + l) // 2
            product = m * m
            if product > x:
                r = m - 1
            elif product < x:
                l = m + 1
                res = m
            else:
                return m

        return res
            