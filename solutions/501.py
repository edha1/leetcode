# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        counts = {}  

        def dfs(node):
            if not node:
                return

            counts[node.val] = counts.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_count = max(counts.values())

        return [val for val, cnt in counts.items() if cnt == max_count]
