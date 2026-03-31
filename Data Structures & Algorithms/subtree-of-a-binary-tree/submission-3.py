# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#root=[1,2,3,4,5]
#subRoot=[2,4,5]
#Expected output: true
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        if self.isSameTrees(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

    def isSameTrees(self, root, subroot):
        if not root and not subroot:
            return True
        
        if not root or not subroot:
            return False

        if root.val == subroot.val:
            return self.isSameTrees(root.left, subroot.left) and self.isSameTrees(root.right, subroot.right)
