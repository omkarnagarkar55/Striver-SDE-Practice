# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal = True
        def dfs(root):
            nonlocal isBal
            if root == None:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)

            if isBal and abs(lh - rh) > 1:
                isBal = False
            return 1 + max(lh,rh) 
        
        dfs(root)
        return isBal