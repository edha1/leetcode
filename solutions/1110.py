# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        forest = []

        def helper(node, is_root):
            if not node:
                return None
            
            deleted = node.val in to_delete_set
            
            if is_root and not deleted:
                forest.append(node)
            
            # Children are roots if current node is deleted
            node.left = helper(node.left, deleted)
            node.right = helper(node.right, deleted)
            
            # Return None if deleted to remove this node
            return None if deleted else node

        helper(root, True)
        return forest
