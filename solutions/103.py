from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        arr = []
        direction = 0  # 0 means left to right, 1 means right to left
        
        while q:
            level_size = len(q)
            curr = []
            
            for _ in range(level_size):
                if direction == 0:
                    # pop from the left
                    node = q.popleft()
                    curr.append(node.val)
                    # append children left to right
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    # pop from the right
                    node = q.pop()
                    curr.append(node.val)
                    # append children in reverse order to the left side
                    # When popping from right, add children in reverse order to the left
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                        
            arr.append(curr)

            if direction == 0: 
                direction = 1 
            else: 
                direction = 0 
            
        return arr
