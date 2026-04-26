class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        N = len(temperatures)
        res = []

        # 1. check if current temp is smaller than top of stack
        # 2. if not smaller, keep popping until larger element appears
        # 3. once larger appears, add difference of indices to res arr

        for i in range(N-1, -1, -1):
            currTemp = temperatures[i]
            
            while len(stack) and currTemp >= temperatures[stack[-1]]:
                stack.pop()

            if len(stack) == 0:
                res.append(0)
                stack.append(i)
                continue

            res.append(stack[-1] - i)
            stack.append(i)

        return res[::-1]

