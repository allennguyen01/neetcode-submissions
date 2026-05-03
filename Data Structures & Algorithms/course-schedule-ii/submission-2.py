class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            adjList[a].append(b)

        # adjList: [[], [0], []]

        path = set()
        visited = set()
        order = []

        # Return True if has cycle
        def dfs(node) -> bool:
            if node in path:
                return True
            if node in visited:
                return False

            path.add(node)

            for nei in adjList[node]:
                if dfs(nei):
                    return True

            order.append(node)
            path.remove(node)
            visited.add(node)

            return False
            
        for course in range(numCourses):
            if dfs(course):
                return []

        return order
        # Time: O(V+E)
        # Space: O(V+E)