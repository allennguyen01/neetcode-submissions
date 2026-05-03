class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)]
        indegrees = [0] * numCourses

        for a, b in prerequisites:
            adjList[b].append(a)
            indegrees[a] += 1
        
        queue = deque()
        for i, degrees in enumerate(indegrees):
            if degrees == 0:
                queue.append(i)

        # print('adjList:', adjList) # [[1], [], []]
        # print('indegrees:', indegrees) # [0, 1, 0]
        # print('queue:', queue) # [0, 2]

        order = []
        processed = 0

        while queue:
            course = queue.popleft()
            order.append(course)
            processed += 1

            for nei in adjList[course]:
                if indegrees[nei]:
                    indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
            
        return order if processed == numCourses else []