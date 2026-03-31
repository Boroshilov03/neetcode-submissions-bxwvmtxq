# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        levels = 0
        dq = deque([root])

        while dq:
            for i in range(len(dq)):
                node = dq.popleft() #2,3
                if node.left:
                    dq.append(node.left) 
                if node.right:
                    dq.append(node.right)
            levels+=1
        return levels