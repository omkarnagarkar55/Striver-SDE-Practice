# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p1, q1):
            if p1 == None or q1 == None:
                return p1 == q1
            
            return (p1.val == q1.val) and check(p1.left,q1.left) and check(p1.right,q1.right)
        return check(p,q)

        