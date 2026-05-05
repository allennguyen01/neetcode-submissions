# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxPathValue = -100

        def dfs(root, maxPathValue):
            if not root: return 0
            isGood = False
            if root.val >= maxPathValue:
                isGood = True
                maxPathValue = root.val
            # print("root:", root.val, "maxValue:", maxPathValue)

            left = dfs(root.left, maxPathValue)
            right = dfs(root.right, maxPathValue)
            return (1 if isGood else 0) + left + right

        return dfs(root, maxPathValue)