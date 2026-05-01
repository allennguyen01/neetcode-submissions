class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        path = set()

        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[a].append(b)

        def dfs(node) -> bool:
            if node in visited:
                return False
            if node in path:
                return True

            path.add(node)
            for nei in adjList[node]:
                hasCycle = dfs(nei)
                if hasCycle:
                    return True

            visited.add(node)
            path.remove(node)
            return False

        for node in range(numCourses):
            if dfs(node):
                return False

        return True 
