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
        #
        if not root:
            return False

        if not subRoot:
            return True

        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]):
        if not a and not b:
            return True

        if a and b and a.val == b.val:
            return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right) 


            

            



