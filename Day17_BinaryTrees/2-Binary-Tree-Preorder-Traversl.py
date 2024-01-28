# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(cur):
            if cur == None:
                return
            
            ans.append(cur.val)
            preorder(cur.left)
            preorder(cur.right)
        
        preorder(root)
        return ans
        