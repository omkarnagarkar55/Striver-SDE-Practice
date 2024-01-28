# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Definition for a binary tree node.
        ans = []
        def postorder(cur):
            if cur == None:
                return
            postorder(cur.left)
            postorder(cur.right)
            ans.append(cur.val)
        postorder(root)
        return ans
        
        