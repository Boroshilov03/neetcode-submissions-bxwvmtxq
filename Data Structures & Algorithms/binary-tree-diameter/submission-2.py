# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        diameter = leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        diameter = max(sub, diameter)
        return diameter

    def height(self, node):
        if not node:
            return 0
        
        return 1 + max(self.height(node.left), self.height(node.right))
