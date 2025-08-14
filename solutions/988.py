# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        
        # dfs and find the lowest path? 

        ## A better approach is to keep track of smallest string, and simply update when we reach a leaf 
        # instead of making a list!
        final = []
        self.dfs(root, [], final)

        return min(final)
    
    def dfs(self, node, path, final):
        if node is None:
            return
        
        path.append(chr(node.val + ord('a')))
        

        if node.left is None and node.right is None:
            final.append(''.join(path[::-1])) 
        
        self.dfs(node.left, path, final)
        self.dfs(node.right, path, final)
        
        # Backtrack
        path.pop()