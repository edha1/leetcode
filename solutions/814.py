class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return self.postOrderPrune(root)
        
    def postOrderPrune(self, root): 
        if root is None:
            return None

        root.left = self.postOrderPrune(root.left)
        root.right = self.postOrderPrune(root.right)

        if root.val == 0 and root.left is None and root.right is None:
            return None  # prune this node

        return root  # keep this node
