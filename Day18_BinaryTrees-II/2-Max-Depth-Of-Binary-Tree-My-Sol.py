# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        def inorder(root,level):
            nonlocal maxD
            if root== None:
                return
            
            inorder(root.left,level + 1)
            inorder(root.right,level + 1)

            maxD = max(maxD,level)
        inorder(root,1)
        return maxD